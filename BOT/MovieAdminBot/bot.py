from decouple import config
from telebot import TeleBot

from app.db.db import Base, engine
from app.menu.menu import Menu
from app.models.model_movie import Movies  # noqa: F401
from app.models.model_user import Users  # noqa: F401
from app.services.service_movie import MovieService
from app.services.service_user import UserServices

TOKEN_BOT = config("TOKEN_BOT")
ADMIN_ID = config("ADMIN_ID")
CHANNEL_ID = config("CHANNEL_ID")

Base.metadata.create_all(engine)

bot = TeleBot(TOKEN_BOT)


@bot.message_handler(commands=["start"])
def start(msg):
    data = {
        "user_id": msg.from_user.id,
        "first_name": msg.from_user.first_name,
        "last_name": msg.from_user.last_name,
        "username": msg.from_user.username,
    }
    UserServices.save_user(data)

    if msg.from_user.id == int(ADMIN_ID):
        bot.send_message(
            msg.chat.id, f"Welcome {msg.from_user.first_name}", reply_markup=Menu.main()
        )
    else:
        bot.send_message(
            msg.chat.id, f"Welcome {msg.from_user.first_name}\nCan I help you?"
        )


@bot.message_handler(func=lambda msg: msg.text == "BACK MENU")
def back(msg):
    if msg.from_user.id == int(ADMIN_ID):
        bot.send_message(msg.chat.id, "Menu", reply_markup=Menu.main())


""" MOVIE """


@bot.message_handler(func=lambda msg: msg.text == "MOVIE")
def movie(msg):
    if msg.from_user.id == int(ADMIN_ID):
        bot.send_message(msg.chat.id, "MOVIE", reply_markup=Menu.movie())


@bot.message_handler(func=lambda msg: msg.text == "ADD MOVIE")
def add_movie(msg):
    if msg.from_user.id == int(ADMIN_ID):
        bot.reply_to(msg, "Send movie file")


@bot.message_handler(content_types=["video"])
def call_add_movie(msg):
    if msg.from_user.id == int(ADMIN_ID):
        check = MovieService.check_movie(msg.video.file_id)
        if check:
            bot.reply_to(msg, "Bu vedio bazada mavjud.")
        else:
            code = MovieService.code_gen_id()

            caption = msg.caption or ""
            title = caption
            description = ""

            file_id = msg.video.file_id
            duration = msg.video.duration
            file_size = msg.video.file_size

            views_count = 0

            data = {
                "code": code,
                "title": title,
                "description": description,
                "file_id": file_id,
                "duration": duration,
                "file_size": file_size,
                "views_count": views_count,
            }
            movie = MovieService.save_movie(data)

            if movie:
                bot.reply_to(msg, f"Movie Code: {movie.code}")
                bot.send_video(
                    CHANNEL_ID,
                    movie.file_id,
                    caption=(f"🎬 {movie.title}\n🔢 Code: {movie.code}"),
                )


@bot.message_handler(func=lambda msg: msg.text == "SHOW MOVIE ALL")
def show_movie_all(msg):
    if msg.from_user.id == int(ADMIN_ID):
        movies = MovieService.show_movie_all_db()
        if movies:
            bot.reply_to(msg, f"<<< MOVIES >>> [ {len(movies)} dona ]")
            for i, movie in enumerate(movies, start=1):
                bot.send_message(msg.chat.id, f"{i}. Code: {movie.code}")
        else:
            bot.reply_to(msg, "Hali kino mavjud emas.")


@bot.message_handler(func=lambda msg: msg.text == "SHOW MOVIE ID")
def show_movie_by_id(msg):
    if msg.from_user.id == int(ADMIN_ID):
        bot.reply_to(msg, "Movie code ni kiriting:")
        bot.register_next_step_handler(msg, show_movie_by_id_call)


def show_movie_by_id_call(msg):
    if msg.from_user.id == int(ADMIN_ID):
        movie = MovieService.show_movie_by_id_db(int(msg.text))

        if movie:
            bot.reply_to(
                msg,
                f"🎬 {movie['title']}\n"
                f"🔢 Code: {movie['code']}\n"
                f"👁 Views: {movie['views_count']}",
            )
        else:
            bot.reply_to(msg, "Movie not found")


""" USER """


@bot.message_handler(func=lambda msg: msg.text == "USER")
def user(msg):
    if msg.from_user.id == int(ADMIN_ID):
        bot.send_message(msg.chat.id, "USERS", reply_markup=Menu.user())


@bot.message_handler(func=lambda msg: msg.text == "USER ALL")
def user_all(msg):
    if msg.from_user.id == int(ADMIN_ID):
        users = UserServices.users_db()
        bot.reply_to(msg, f"<<< USERS >>> [ {len(users)} dona ]")
        for i, user in enumerate(users, start=1):
            bot.send_message(msg.chat.id, f"{i}. {user.first_name}\nID: {user.user_id}")


@bot.message_handler(func=lambda msg: msg.text == "USER ID")
def user_by_id(msg):
    if msg.from_user.id == int(ADMIN_ID):
        bot.send_message(msg.chat.id, "User ID ni kiriting:")
        bot.register_next_step_handler(msg, user_by_id_call)


def user_by_id_call(msg):
    user = UserServices.user_id_db(int(msg.text))

    if user:
        bot.send_message(msg.chat.id, f"{user.first_name}")
    else:
        bot.send_message(msg.chat.id, "User not found!")


""" STATISTIC """


@bot.message_handler(func=lambda msg: msg.text == "STATISTIC")
def statistic(msg):
    if msg.from_user.id == int(ADMIN_ID):
        user_count = UserServices.statistic_user_count()
        movie_count = MovieService.statistic_movie_count()
        bot.send_message(
            msg.chat.id,
            f"📊 STATISTIC\n\n👤 Users: {user_count}\n🎬 Movies: {movie_count}",
        )


print("Bot is running...")
bot.infinity_polling()

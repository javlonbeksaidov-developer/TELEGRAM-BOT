from decouple import config
from telebot import TeleBot

from app.db.db import Base, engine, get_db
from app.menu.menu import Menu
from app.models.model_movie import Movies  # noqa: F401
from app.models.model_user import Users

TOKEN_BOT = config("TOKEN_BOT")
ADMIN_ID = config("ADMIN_ID")

Base.metadata.create_all(engine)

bot = TeleBot(TOKEN_BOT)


@bot.message_handler(commands=["start"])
def start(msg):
    user_id = msg.from_user.id
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    username = msg.from_user.username

    with get_db() as db:
        user = db.query(Users).filter(Users.user_id == msg.from_user.id).first()

        if not user:
            user = Users(
                first_name=first_name,
                last_name=last_name,
                user_id=user_id,
                username=username,
            )
            db.add(user)
            db.commit()
            db.refresh(user)
        else:
            if (
                user.username != username
                or user.first_name != first_name
                or user.last_name != last_name
            ):
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                db.commit()

    if user_id == int(ADMIN_ID):
        bot.send_message(
            msg.chat.id, f"Welcome {msg.from_user.first_name}", reply_markup=Menu.main()
        )
    else:
        bot.send_message(
            msg.chat.id, f"Welcome {msg.from_user.first_name}\nCan I help you?"
        )


@bot.message_handler(func=lambda msg: msg.text == "BACK MENU")
def back(msg):
    bot.send_message(msg.chat.id, "Menu", reply_markup=Menu.main())


""" MOVIE """


@bot.message_handler(func=lambda msg: msg.text == "MOVIE")
def movie(msg):
    bot.send_message(msg.chat.id, "MOVIE", reply_markup=Menu.movie())


@bot.message_handler(func=lambda msg: msg.text == "ADD MOVIE")
def add_movie(msg):
    bot.reply_to(msg, "Kino qo'shish")


@bot.message_handler(func=lambda msg: msg.text == "SHOW MOVIE ALL")
def show_movie_all(msg):
    bot.reply_to(msg, "Kinolar ro'yhati")


@bot.message_handler(func=lambda msg: msg.text == "SHOW MOVIE ID")
def show_movie_by_id(msg):
    bot.reply_to(msg, "Kino Ma'lumoti")


""" USER """


@bot.message_handler(func=lambda msg: msg.text == "USER")
def user(msg):
    bot.send_message(msg.chat.id, "USERS", reply_markup=Menu.user())


@bot.message_handler(func=lambda msg: msg.text == "USER ALL")
def user_all(msg):
    with get_db() as db:
        users = db.query(Users).all()

        for user in users:
            bot.reply_to(msg, user.first_name)


@bot.message_handler(func=lambda msg: msg.text == "USER ID")
def user_by_id(msg):
    bot.reply_to(msg, "Foydalanuvchi ma'lumoti")


@bot.message_handler(func=lambda msg: msg.text == "user_by_id")
def user_by_id_call(msg):
    bot.reply_to(msg, "Foydalanuvchi ma'lumoti")


""" STATISTIC """


@bot.message_handler(func=lambda msg: msg.text == "STATISTIC")
def statistic(msg):
    bot.send_message(msg.chat.id, "Ma'lumot topilmadi!")


print("Bot is running...")
bot.infinity_polling()

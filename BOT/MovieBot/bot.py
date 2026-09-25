from decouple import config
from telebot import TeleBot

from app.services.service_movie import MovieService
from app.services.service_user import UserServices

TOKEN_BOT = config("TOKEN_BOT")
CHANNEL_ID = config("CHANNEL_ID")

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

    bot.send_message(
        msg.chat.id, f"Welcome {msg.from_user.first_name}\nCan I help you?"
    )


@bot.message_handler(commands=["help"])
def help(msg):
    bot.send_message(msg, "Movie ID sini kiriting!\n(Misol uchun [ 17 ])")


@bot.message_handler(func=lambda msg: msg.text.isdigit())
def id_movie_send(msg):
    movie = MovieService.show_movie_by_code(int(msg.text))

    if movie:
        bot.send_video(
            msg.chat.id,
            movie["file_id"],
            caption=(
                f"🎬 {movie['title']}\n"
                f"🔢 Code: {movie['code']}\n"
                f"👁 Views: {movie['views_count']}"
            ),
        )
    else:
        bot.send_message(msg.chat.id, "Movie not found!")

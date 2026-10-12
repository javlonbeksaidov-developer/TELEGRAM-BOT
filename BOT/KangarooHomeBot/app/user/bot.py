from telebot import TeleBot

from .keyboards import Keyboards
from .models import UserRoles, Users  # noqa: F401
from .services import UserServices


def register_handlers(bot: TeleBot):

    @bot.message_handler(commands=["start"])
    def welcome(msg):
        user_id = msg.from_user.id
        first_name = msg.from_user.first_name
        last_name = msg.from_user.last_name or ""
        tg_username = msg.from_user.username or ""

        data = {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "tg_username": tg_username,
        }

        user = UserServices.save_user(data)
        if user:
            bot.send_message(
                msg.chat.id,
                "Assalomu alaykum! Kangaroo Home botiga xush kelibsiz 🏠",
                reply_markup=Keyboards.register(),
            )

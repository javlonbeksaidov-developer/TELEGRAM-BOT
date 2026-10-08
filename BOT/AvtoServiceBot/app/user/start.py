from telebot import TeleBot

from keyboards.admin import AdminKeyboards
from services.admin_service import AdminServices
from services.user_service import UserServices


def register_handlers(bot: TeleBot):

    @bot.message_handler(commands=["start"])
    def start_command(msg):
        user_id = msg.from_user.id
        first_name = msg.from_user.first_name or ""
        last_name = msg.from_user.last_name or ""
        username = msg.from_user.username or ""

        data = {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
        }

        user = UserServices.save_user(data)
        admin = AdminServices.is_admin(msg.from_user.id)

        if admin:
            bot.send_message(
                msg.chat.id,
                f"Welcome Capitan {msg.from_user.first_name}!",
                reply_markup=AdminKeyboards.main_keyboard(),
            )
        elif user:
            bot.send_message(
                msg.chat.id,
                f"Assalomu alaykum! {msg.from_user.first_name}\n🚗 Avto Service Botga xush kelibsiz.",
            )
        else:
            bot.send_message(
                msg.chat.id,
                "...",
            )

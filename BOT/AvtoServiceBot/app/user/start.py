from telebot import TeleBot

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

        UserServices.save_user(data)

        bot.send_message(
            msg.chat.id,
            f"Assalomu alaykum! {msg.from_user.first_name}\n🚗 Avto Service Botga xush kelibsiz.",
        )

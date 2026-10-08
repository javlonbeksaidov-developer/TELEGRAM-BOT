from telebot import TeleBot

from keyboards.admin import AdminKeyboards
from services.admin_service import AdminServices
from services.user_service import UserServices


def register_handlers(bot: TeleBot):

    @bot.message_handler(commands=["start"])
    def start_admin(msg):
        admin = AdminServices.is_admin(msg.from_user.id)

        if admin:
            bot.send_message(
                msg.chat.id,
                f"Welcome Capitan {msg.from_user.first_name}!",
                reply_markup=AdminKeyboards.main_keyboard(),
            )

    @bot.message_handler(func=lambda msg: msg.text == "STATISTIC")
    def statistic(msg):
        admin = AdminServices.is_admin(msg.from_user.id)

        if admin:
            admins = AdminServices.admin_count()
            users = UserServices.user_count()
            bot.reply_to(
                msg, f"📊 Statistic Users!\n\n👤 Users: {users}\n👨‍💼 Admins: {admins}"
            )

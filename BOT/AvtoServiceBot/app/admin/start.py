from telebot import TeleBot

from keyboards.admin import AdminKeyboards
from services.admin_service import AdminServices
from services.user_service import UserServices


def register_handlers(bot: TeleBot):

    @bot.message_handler(func=lambda msg: msg.text == "STATISTIC")
    def statistic(msg):
        admin = AdminServices.is_admin(msg.from_user.id)
        if admin:
            admins = AdminServices.admin_count()
            users = UserServices.user_count()
            bot.reply_to(
                msg, f"📊 Statistic Users!\n\n👤 Users: {users}\n👨‍💼 Admins: {admins}"
            )

    @bot.message_handler(func=lambda msg: msg.text == "USERS MANAGEMENT")
    def users_management(msg):
        admin = AdminServices.is_admin(msg.from_user.id)
        if admin:
            bot.send_message(
                msg.chat.id, msg.text, reply_markup=AdminKeyboards.users_keyboard()
            )

    @bot.message_handler(func=lambda msg: msg.text == "USER_TO_ADMIN")
    def handler_user_to_admin(msg):
        admin = AdminServices.is_admin(msg.from_user.id)
        if admin:
            bot.send_message(
                msg.chat.id, "👤 Admin role berish uchun foydalanuvchi ID'sini yozing:"
            )

            bot.register_next_step_handler(msg, user_to_admin)

    def user_to_admin(msg):
        admin = AdminServices.is_admin(msg.from_user.id)

        if admin:
            user_id = msg.text.strip()
            UserServices.user_to_admin(user_id)
            bot.send_message(msg.chat.id, "✅ Foydalanuvchiga ADMIN role berildi.")

    @bot.message_handler(func=lambda msg: msg.text == "ADMIN_TO_USER")
    def handler_admin_to_user(msg):
        admin = AdminServices.is_admin(msg.from_user.id)
        if admin:
            bot.send_message(
                msg.chat.id, "👤 Foydalanuvchi role berish uchun Admin ID'sini yozing:"
            )

            bot.register_next_step_handler(msg, admin_to_user)

    def admin_to_user(msg):
        admin = AdminServices.is_admin(msg.from_user.id)

        if admin:
            user_id = msg.text.strip()
            AdminServices.admin_to_user(user_id)
            bot.send_message(msg.chat.id, "✅ Adminga USER role berildi.")

    @bot.message_handler(func=lambda msg: msg.text == "GOO")
    def goo(msg):
        chat_id = 6467651270
        bot.send_message(chat_id, "✅ Foydalanuvchiga ADMIN role berildi.")

from decouple import config
from telebot import TeleBot

from database.db import Base, engine
from database.models import Users  # noqa: F401

BOT_TOKEN = config("BOT_TOKEN")


bot = TeleBot(BOT_TOKEN)

Base.metadata.create_all(bind=engine)

from app.admin.start import register_handlers as register_admin_start
from app.user.start import register_handlers as register_user_start

register_admin_start(bot)
register_user_start(bot)


if __name__ == "__main__":
    print("🚗 Avto Service Bot is running...")
    bot.infinity_polling()

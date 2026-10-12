from decouple import config
from telebot import TeleBot

from app.user.bot import register_handlers as user
from app.user.models import Role, UserRoles, Users  # noqa: F401
from config.db import Base, engine

BOT_TOKEN = config("BOT_TOKEN")

bot = TeleBot(token=BOT_TOKEN)

Base.metadata.create_all(engine)

user(bot)


if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()

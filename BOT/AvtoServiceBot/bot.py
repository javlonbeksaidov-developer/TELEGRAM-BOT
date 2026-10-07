from decouple import config
from telebot import TeleBot

BOT_TOKEN = config("BOT_TOKEN")


bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome(msg):
    bot.send_message(msg.chat.id, msg.from_user.first_name)


if __name__ == "__main__":
    print("🚗 Avto Service Bot is running...")
    bot.infinity_polling()

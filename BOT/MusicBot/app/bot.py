from decouple import config
from telebot import TeleBot

BOT_TOKEN=config("BOT_TOKEN")

bot = TeleBot(token=BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, f"Hi {msg.from_user.first_name}, Can I help you?")



print("BOT is running...")
bot.infinity_polling()
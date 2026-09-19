import random

from btns import main_buttons
from decouple import config
from telebot import TeleBot

BOT_TOKEN = config("BOT_TOKEN")

bot = TeleBot(token=BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, "Welcome to Random Number Bot!", reply_markup=main_buttons())


@bot.message_handler(func=lambda _: True)
def handle_buttons(msg):
    match msg.text:
        case "0-10":
            number = random.randint(0, 10)
            bot.reply_to(msg, f"Random number: {number}")
        case "0-100":
            number = random.randint(0, 100)
            bot.reply_to(msg, f"Random number: {number}")
        case "0-1000":
            number = random.randint(0, 1000)
            bot.reply_to(msg, f"Random number: {number}")
        case "0-10000":
            number = random.randint(0, 10000)
            bot.reply_to(msg, f"Random number: {number}")
        case "Other":
            bot.reply_to(msg, "Entry: start-stop. (0-10)")


@bot.message_handler(func=lambda _: True)
def start_stop(msg):
    start, stop = map(int, msg.split("-"))
    if start <= stop:
        number = random.randint(start, stop)
        bot.reply_to(msg, f"[{start}-{stop}] -> Random number: {number}")


print("Bot is running...")
bot.infinity_polling()

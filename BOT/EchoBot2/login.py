from decouple import config
from telebot import TeleBot, types

TOKEN_BOT = config("TOKEN_BOT")
bot = TeleBot(token=TOKEN_BOT)

users_db = {}


def menu():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Ro'yxatdan o'tish")
    markup.row(btn1)
    return markup


@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(
        msg.chat.id,
        f"Xush kelibsiz, {msg.from_user.first_name}! Sizga qanday yordam bera olaman?",
        reply_markup=menu(),
    )



print("Bot is running...")
bot.infinity_polling()
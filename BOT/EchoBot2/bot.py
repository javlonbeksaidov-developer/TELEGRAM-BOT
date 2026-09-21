from decouple import config
from telebot import TeleBot, types

TOKEN_BOT = config("TOKEN_BOT")

bot = TeleBot(token=TOKEN_BOT)


def menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("Registration")
    btn2 = types.KeyboardButton("Upload Movie")
    btn3 = types.KeyboardButton("Find Movie")

    markup.row(btn1, btn2, btn3)

    return markup


def inline():
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text="registration", callback_data="register")
    btn2 = types.InlineKeyboardButton(text="Upload Movie", callback_data="upload")
    btn3 = types.InlineKeyboardButton(text="Find Movie", callback_data="find")

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)

    return markup


@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(
        msg.chat.id,
        f"Welocome {msg.from_user.first_name}, Can I help you ?",
        reply_markup=menu(),
    )


@bot.message_handler(func=lambda _: True)
def message(msg):
    bot.reply_to(msg, msg.text, reply_markup=inline())


@bot.callback_query_handler(func=lambda call: call.data == "register")
def call_register(call):
    bot.answer_callback_query(call.id, text="Register !!!")
    bot.send_message(call.message.chat.id, text="Success!")

@bot.callback_query_handler(func=lambda call: call.data == "upload")
def call_upload(call):
    bot.answer_callback_query(call.id, text="Upload !!!")
    bot.send_message(call.message.chat.id, text="Success!")

@bot.message_handler(
    content_types=["photo", "document", "contact", "location", "voice", "audio"]
)
def handle_media(msg):
    bot.reply_to(msg, "Media is saved!")


print("Bot is running...")
bot.infinity_polling()

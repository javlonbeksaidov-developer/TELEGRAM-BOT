import telebot
from decouple import config
from telebot import types

TOKEN = config("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, "HI DEAR!")


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.reply_to(message, "Can I help you?")


# @bot.message_handler(func=handler_message)
# def hadle_message(message):
#     bot.reply_to(message, str(dir(message)))


@bot.message_handler(func=lambda message: message if message.text == "echo" else False)
def hadle_message_echo(message):
    bot.reply_to(message, "Welcome to Echo bot !")


@bot.message_handler(
    func=lambda message: message if message.text == "yashnar" else False
)
def hadle_message_yashnar(message):
    bot.reply_to(message, "Hi, Yash Chopra !")


def markup_():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text="Music")
    button2 = types.KeyboardButton(text="Movie")
    button3 = types.KeyboardButton(text="Film")
    button4 = types.KeyboardButton(text="Podcast")
    button5 = types.KeyboardButton(text="Other")
    button6 = types.KeyboardButton(text="Contack", request_contact=True)
    button7 = types.KeyboardButton(text="Location", request_location=True)

    markup.add(button1, button2, button3, button4)
    markup.add(button6, button7)
    markup.add(button5)

    return markup


@bot.message_handler(func=lambda message: message)
def from_to(message):
    bot.reply_to(message, message.text, reply_markup=markup_())


@bot.message_handler(content_types=["contact"])
def handle_contack(message):
    msg = {
        "full_name": f"{message.contact.first_name} {message.contact.last_name}",
        "phone_number": f"{message.contact.phone_number}",
        "user_id": f"{message.contact.user_id}",
    }
    bot.reply_to(message, str(msg))


print("Bot is running...")
bot.infinity_polling()

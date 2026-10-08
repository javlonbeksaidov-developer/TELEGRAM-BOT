from telebot import types


class AdminKeyboards:
    @staticmethod
    def main_keyboard():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1=types.KeyboardButton("STATISTIC")
        btn2=types.KeyboardButton("2")
        btn3=types.KeyboardButton("3")

        markup.add(btn1, btn2, btn3)
        return markup
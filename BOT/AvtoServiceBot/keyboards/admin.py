from telebot import types


class AdminKeyboards:
    @staticmethod
    def main_keyboard():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1=types.KeyboardButton("STATISTIC")
        btn2=types.KeyboardButton("USERS MANAGEMENT")
        btn3=types.KeyboardButton("GOO")

        markup.add(btn1, btn2, btn3)
        return markup

    @staticmethod
    def users_keyboard():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("USER_TO_ADMIN")
        btn2 = types.KeyboardButton("ADMIN_TO_USER")
        btn3 = types.KeyboardButton("BACK")

        markup.add(btn1, btn2, btn3)
        return markup
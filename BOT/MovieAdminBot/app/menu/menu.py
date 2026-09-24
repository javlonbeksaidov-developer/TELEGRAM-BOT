from telebot import types


class Menu:
    @staticmethod
    def main():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("MOVIE")
        btn2 = types.KeyboardButton("USER")
        btn3 = types.KeyboardButton("STATISTIC")

        markup.add(btn1, btn2)
        markup.add(btn3)

        return markup

    @staticmethod
    def movie():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("ADD MOVIE")
        btn2 = types.KeyboardButton("SHOW MOVIE ALL")
        btn3 = types.KeyboardButton("SHOW MOVIE ID")
        btn4 = types.KeyboardButton("BACK MENU")

        markup.add(btn1, btn2, btn3)
        markup.add(btn4)

        return markup

    @staticmethod
    def user():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("USER ALL")
        btn2 = types.KeyboardButton("USER ID")
        btn3 = types.KeyboardButton("BACK MENU")

        markup.add(btn1, btn2)
        markup.add(btn3)

        return markup

from telebot import types


def main_buttons():
    main_btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn1 = types.KeyboardButton("0-10")
    btn2 = types.KeyboardButton("0-100")
    btn3 = types.KeyboardButton("0-1000")
    btn4 = types.KeyboardButton("0-10000")
    btn5 = types.KeyboardButton("Other")

    main_btn.add(btn1, btn2, btn3, btn4)
    main_btn.add(btn5)

    return main_btn
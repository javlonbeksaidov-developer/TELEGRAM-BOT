from telebot.types import KeyboardButton, ReplyKeyboardMarkup


class Keyboards:
    @staticmethod
    def register():
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        markup.add(
            KeyboardButton("🏠 Uy qidirish"),
            KeyboardButton("🗺 Xarita"),
        )
        markup.add(
            KeyboardButton("📝 Ro'yhatdan o'tish"),
            KeyboardButton("☎️ Menejer bilan aloqa"),
        )

        return markup

    @staticmethod
    def main_menu():
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        markup.add(
            KeyboardButton("🏠 Uy qidirish"),
            KeyboardButton("🗺 Xarita"),
            KeyboardButton("❤️ Sevimlilar"),
            KeyboardButton("💳 To'lovlarim"),
            KeyboardButton("📋 Murojaatlarim"),
            KeyboardButton("📅 Uchrashuvlarim"),
            KeyboardButton("👤 Mening profilim"),
            KeyboardButton("☎️ Menejer bilan aloqa"),
        )

        return markup

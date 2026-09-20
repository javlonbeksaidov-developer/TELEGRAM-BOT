from app.music.models import Musics  # noqa: F401
from app.music.services import MusicServices
from app.user.models import Users  # noqa: F401
from app.user.services import UserServices
from db.database import Base, engine
from decouple import config
from telebot import TeleBot

BOT_TOKEN = config("BOT_TOKEN")
CHANNEL_ID = config("CHANNEL_ID", cast=int)

Base.metadata.create_all(engine)

bot = TeleBot(token=BOT_TOKEN)

""" USER """


@bot.message_handler(commands=["start"])
def start(msg):
    user_id = msg.from_user.id
    username = msg.from_user.username
    first_name = msg.from_user.first_name or ""
    last_name = msg.from_user.last_name or ""

    full_name = f"{first_name} {last_name}".strip()

    data = {
        "user_id": user_id,
        "username": username,
        "full_name": full_name,
    }
    UserServices.save_user(data)

    bot.reply_to(msg, f"Hi {msg.from_user.first_name}, Can I help you?")


@bot.message_handler(commands=["info"])
def info(msg):
    user_id = msg.from_user.id
    username = msg.from_user.username
    first_name = msg.from_user.first_name or ""
    last_name = msg.from_user.last_name or ""

    full_name = f"{first_name} {last_name}".strip()

    data = {
        "user_id": user_id,
        "username": username,
        "full_name": full_name,
    }
    user = UserServices.user_info(data)

    bot.reply_to(msg, user)


""" MUSIC """


@bot.channel_post_handler(content_types=["audio", "document"])
@bot.message_handler(content_types=["audio", "document"])
def save_music(msg):
    if msg.chat.id == CHANNEL_ID:
        media = msg.audio or msg.document

        if media:
            title = (
                getattr(media, "title", None)
                or getattr(media, "file_name", None)
                or "Noma'lum qo'shiq"
            )
            performer = getattr(media, "performer", None) or "Noma'lum san'atkor"

            data = {
                "file_id": media.file_id,
                "title": title,
                "performer": performer,
                "file_name": getattr(media, "file_name", None),
                "duration": getattr(media, "duration", 0),
                "file_size": getattr(media, "file_size", 0),
            }

            saved_music = MusicServices.save_music(data)
            if saved_music:
                print(
                    f"✅ Bazaga qo'shildi: {saved_music.performer} - {saved_music.title}"
                )


@bot.message_handler(func=lambda msg: msg.text and msg.text.isdigit())
def search_by_id_handler(msg):
    music_id = int(msg.text.strip())

    music = MusicServices.search_by_id(music_id)

    if not music:
        bot.reply_to(msg, "❌ Bunday ID ga ega musiqa topilmadi.")
        return

    bot.send_audio(
        chat_id=msg.chat.id,
        audio=music.file_id,
        caption=f"🎵: {music.title}\n🆔: {music.id}",
        parse_mode="HTML",
        reply_to_message_id=msg.message_id,
    )


@bot.message_handler(
    func=lambda msg: (
        msg.text and not msg.text.startswith("/") and not msg.text.isdigit()
    )
)
def search_by_title(msg):
    text = msg.text.strip()
    if len(text) <= 2:
        bot.reply_to(msg, "⚠️ Iltimos, qidirish uchun 3 tadan ko'proq harf kiriting!")
        return

    musics = MusicServices.search_by_title(msg.text.strip())

    if not musics:
        bot.reply_to(msg, "❌ Bunday musiqa topilmadi.")
        return

    bot.reply_to(msg, f"<< {text} >> musiqalar.\nJami: {len(musics)} ta.")

    for music in musics:
        bot.send_message(msg.chat.id, f"🆔: {music.id}.\n🎵: {music.title}")


print("BOT is running...")
bot.infinity_polling()

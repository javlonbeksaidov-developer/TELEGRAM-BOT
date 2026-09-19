import asyncio

from decouple import config
from telebot.async_telebot import AsyncTeleBot

from translator import translate

BOT_TOKEN = config("BOT_TOKEN")
bot = AsyncTeleBot(token=BOT_TOKEN)


@bot.message_handler(commands=["start"])
async def start(msg):
    await bot.reply_to(msg, text="Welocome to Google Translator Bot!")


@bot.message_handler(func=lambda message: True)
async def handle_translate(msg):
    translated_text = await translate(msg.text)
    await bot.reply_to(msg, text=translated_text)


async def main():
    print("Bot is running...")
    await bot.polling(non_stop=True)


if __name__ == "__main__":
    asyncio.run(main())

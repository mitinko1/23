import asyncio
import logging
import sys
import requests

from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import CommandStart
from aiogram.types import Message

dispatcher = Dispatcher()
bot = Bot("6708171543:AAGzgZhcUFiugtUu17s5HrRe1Pfcmh0zcEc")

@dispatcher.message(F.text == "Дай кота!")
async def image_hundler(message: Message):
    responce = requests.get("https://api.thecatapi.com/v1/images/search").json()
    await message.answer_photo(responce[0]["url"])

@dispatcher.message(CommandStart())
async def command_start_handler(message: Message):
    keyboarCats = [
        [
            types.KeyboardButton(text = "Хочу, котика!")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=keyboarCats,
        resize_keyboard=True,
        input_field_placeholder="Котики"
    )

    await message.answer("Привет!")

async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
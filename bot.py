import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

game_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🎮 Играть", web_app=WebAppInfo(url="https://ваш-сайт.ru"))]],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🚗 Нажми 'Играть'!", reply_markup=game_keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
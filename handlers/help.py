from aiogram import types
from aiogram.types import ParseMode
from config import HELP_MESSAGE
from loader import dp


@dp.message_handler(text='\U0001F691 Помощь')
async def bot_help(message: types.Message):
    await message.answer(HELP_MESSAGE.replace('%username%', message.from_user.username), parse_mode=ParseMode.HTML)
    #  Тут ничего интересного: идёт описание основных функций бота обычному смертному юзеру. Скука страшная...
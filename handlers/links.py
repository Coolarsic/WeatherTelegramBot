from aiogram import types
from loader import dp, bot
from keyboards import inline_keyboard


@dp.message_handler(text='\U0001F4C1 Репозиторий')
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, text='Тут просто наш ссылка на наш github-репозиторий', reply_markup=inline_keyboard)
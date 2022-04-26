from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from forms.user import User
from data import db_session
from config import SAD_ART
from loader import dp, bot


class FSMCity(StatesGroup):
    city = State()


@dp.message_handler(text='\U0001F3D9 Сменить город', state=None)
async def cm_start(message: types.Message):
    await FSMCity.city.set()
    await message.reply('Напишите название города')


@dp.message_handler(state=FSMCity.city)
async def get_city(message: types.Message, state: FSMContext):
    try:
        session = db_session.create_session()
        user = session.query(User).filter(message.from_user.id == User.chat_id).first()
        user.town = message.text
        session.commit()
        session.close()
        await message.reply('Название города сохранено')
        await state.finish()
        #  открываем сессию, сохраняем город юзера и закрываем сессию. Не забываем остановить маштину состояний.
    except Exception:
        await bot.send_message(message.from_user.id, 'Извините, что-то пошло не так...' + SAD_ART)
        await state.finish()
        #  если вдруг что-то произошло не допускаем падения бота. Снова не забываем про остановку машины состояний.

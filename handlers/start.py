from aiogram import types
from forms.user import User
from data import db_session
from loader import dp, bot
from keyboards import start_keyboard


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Добрый день.", reply_markup=start_keyboard) #  приветствуем юзера
    session = db_session.create_session()
    if session.query(User).filter(message.from_user.id == User.chat_id).first() is None:
        user = User()
        user.name = message.from_user.username
        user.town = 'Москва'
        user.chat_id = message.from_user.id
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        db_sess.close()
        #  открываем сессию БД, ставим по дефолту юзеру город - Москву и закрываем сессию.

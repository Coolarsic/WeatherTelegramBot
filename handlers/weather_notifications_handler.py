from aiogram import types
from forms.user import User
from tools.get_user_notifications import get_user_notifications
from data import db_session
from loader import dp, bot


@dp.message_handler(commands=['start_notification'])
async def start_notification(message: types.Message):
    hours = 1
    session = db_session.create_session()
    user = session.query(User).filter(message.from_user.id == User.chat_id).first()
    town = user.town
    user_notifications = await get_user_notifications(message_user_id=message.from_user.id, session=session)
    user_notifications.hours_remain = hours
    user_notifications.is_enable = True
    session.commit()
    session.close()
    await bot.send_message(
        message.from_user.id,
        f"Вам теперь будет отправлятся рассылка погоды города <b>{town}</b> каждые <b>{hours}</b>ч.")




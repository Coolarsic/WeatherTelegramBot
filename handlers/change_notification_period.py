from aiogram import types
from forms.user import User
from data import db_session

from loader import dp, bot
from keyboards import notifications_inline_menu_period
from tools.get_user_notifications import get_user_notifications


@dp.callback_query_handler(text='change_period_notifications')
async def change_period_notifications_handler(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='Отправлять уведомления нужно кажд(ый/ые)',
                                reply_markup=notifications_inline_menu_period)


@dp.callback_query_handler(text_contains='set_notifications_period')
async def switch_notifications_handler(call: types.CallbackQuery):
    hours_count = int(call.data.split('_')[-1])
    session = db_session.create_session()
    user_notifications = await get_user_notifications(call.message.chat.id, session=session)
    user_notifications.period = hours_count
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'Вам будут присылаться уведомления кажд(ый/ые) {hours_count} час(a)!')
    session.commit()
    session.close()
from aiogram import types
from data import db_session
from tools.get_user_notifications import get_user_notifications
from loader import dp, bot


@dp.callback_query_handler(text='switch_notifications')
async def switch_notifications_handler(call: types.CallbackQuery):
    session = db_session.create_session()
    user_notifications = await get_user_notifications(call.message.chat.id, session=session)
    notifications_status = user_notifications.is_enable
    if notifications_status:
        user_notifications.is_enable = False
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Уведомления отключены')
    else:
        user_notifications.is_enable = True
        if user_notifications.period is None:
            user_notifications.period = 1
        if user_notifications.ntype is None:
            user_notifications.ntype = 1
        user_notifications.hours_remain = user_notifications.period
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Уведомления включены')
    session.commit()
    session.close()

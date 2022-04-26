from aiogram import types
from forms.user import User
from data import db_session
from loader import dp, bot
from config import PROFILE_MESSAGE


@dp.message_handler(text='\U0001F464 Профиль')
async def get_weather(message: types.Message):
    session = db_session.create_session()
    user = session.query(User).filter(message.from_user.id == User.chat_id).first()
    town = user.town
    requestsam = user.requestsam
    date = user.register_date
    text_message = PROFILE_MESSAGE.replace('%user_mention%', f'{message.from_user.mention}')
    text_message = text_message.replace('%user_town%', f'{town}')
    text_message = text_message.replace('%user_weather_requests%', f'{requestsam}')
    text_message = text_message.replace('%register_date%', f'{date.strftime("%B %d %Y %H:%M:%S")}')
    UserProfilePhotos = await bot.get_user_profile_photos(message.from_user.id)
    if len(UserProfilePhotos['photos']) == 0:
        await bot.send_message(chat_id=message.from_user.id, text=text_message)
    else:
        await bot.send_photo(chat_id=message.from_user.id, photo=UserProfilePhotos['photos'][0][0]['file_id'], caption=text_message)
    session.commit()
    session.close()
    #  сообщаем юзеру инфу о нём: сколько раз получал погоду, фото профиля и его город

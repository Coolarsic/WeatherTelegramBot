import os
from tools.geocode import get_coords
from config import WEATHER_TOKEN, SAD_ART
from aiogram.types import ParseMode, InputFile
import requests
import json
import numpy as np
import matplotlib.pyplot as plt
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from forms.user import User
from data import db_session
from loader import dp, bot
from PIL import Image
from keyboards import graph_keyboard


@dp.message_handler(text='\U0001F4C8 График температуры')
async def send_keyboard(message: types.Message):
    await bot.send_message(message.from_user.id, "Выберите, на какое количество дней вперёд вам нужен график", reply_markup=graph_keyboard)


@dp.callback_query_handler(text_contains='temp_graph')
async def send_graph(call: types.CallbackQuery):
    try:
        num = int(call.data.split('_')[-1])  # получили число
        session = db_session.create_session()
        user = session.query(User).filter(call.from_user.id == User.chat_id).first()
        town = user.town
        coords = get_coords(town)
        if coords == (None, None):
            raise ValueError
        #  получаем координаты города
        file_to_send = 'https://i.pinimg.com/originals/8d/c7/40/8dc740acec8d184cb4202f059938b92f.jpg'
        sec_message = await bot.send_photo(call.from_user.id, photo=file_to_send, caption='<b>Секундочку...</b>',
                                           parse_mode=ParseMode.HTML)
        #  отправляем сохраняем сообщение, оно нам понадобится. Пока запрос обрабатывается будет висеть другая картинка
        response = json.loads(requests.get(
            f'https://api.weather.yandex.ru/v1/forecast?lat={coords[1]}&lon={coords[0]}&lang=ru_RU&limit=7&hours=true',
            headers={'X-Yandex-API-Key': WEATHER_TOKEN}).content)
        #  получили ответ от сервера
        temps = []  #  здесь будут храниться температуры для выстраивания графика
        for i in response['forecasts'][num]['hours']:
            temps.append(int(i['temp']))
            #  заполняем массив
        fig = plt.figure()
        zero = [-80] * 24
        ax = fig.add_subplot(111)
        ax.set_facecolor('#444444')
        ax.set_ylabel('Температура, °C', fontsize=14)
        ax.set_xlabel('Время', fontsize=14)
        xranges = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
                   '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00',
                   '22:00', '23:00']
        #  подготовили всё для постройки графика
        ax.set_xticks(np.arange(0, 24))
        ax.set_xticklabels(xranges)
        #  расставляем подписи по оси x
        ax.set_yticks(np.arange(-80, 81, 5))
        ax.set_yticklabels(np.arange(-80, 81, 5))
        #  расставляем подписи по оси y
        ax.grid(axis='x', color='#555555')
        #  выставляем сетку
        plt.plot(temps, color='yellow')
        plt.fill_between(xranges, temps, zero, color='#444400')
        #  строим график
        for i in range(len(temps)):
            if i == len(temps) - 1:
                break
            else:
                plt.annotate(f"{str(temps[i])}°C", xy=(i, temps[i]), xytext=(i + 0.1, temps[i] + 2), color='#DDDDDD')
                #  размещаем подписи температуры
        plt.ylim(-80, 80)
        plt.xlim(0, 23)
        fg = plt.gcf()
        fg.set_size_inches(15, 10)
        #  устанавливаем нормальный размер
        ax.patch.set_alpha(0.9)
        fg.patch.set_facecolor('#444444')
        plt.savefig(f'for_user_{call.from_user.id}.jpg')
        #  сохраняем изображение чтобы отправить пользователю
        img1 = Image.open(f'for_user_{call.from_user.id}.jpg')
        pst = Image.open('data/photos/yandex_weather.png').resize((200, 120))
        img1.paste(pst, (675, 0))
        img1.save(f'for_user_{call.from_user.id}.jpg')
        #  накладываем изображение яндекс погоды
        file_to_send = InputFile(f'for_user_{call.from_user.id}.jpg')
        media = types.InputMediaPhoto(media=file_to_send)
        await sec_message.edit_media(media=media)
        await sec_message.edit_caption(caption=f'<b>А вот и график температуры!</b>', parse_mode=ParseMode.HTML)
        #  убираем фотку чела из fallout shelter, ставим график
        os.remove(f'for_user_{call.from_user.id}.jpg')
        #  удаляем нунужный файл
    except Exception as e:
        await bot.send_message(call.from_user.id, "Извините, что-то пошло не так. Проверьте правильность написания города или попробуйте попытку позже" + SAD_ART)
        #  скорее всего пользователь ввёл дичь (например, текст).

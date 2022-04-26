import logging
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from loader import dp, scheduler
from config import ADMINS
from data import db_session
from forms.weather import WeatherNotifications
import handlers


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")
            #  швыряем админам уведомление о том, что бот запущен
        except Exception as err:
            logging.exception(err)
            #  что-то пошло не так, обрабатываем исключение


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("start_notification", "Установить таймер (не готово)"),
            types.BotCommand("links", "Ссылка на наш github")
        ]
    )
    #  как можно догадаться по названию функции - устанавливаем команды бота


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def process_send_weather_notifications():
    session = db_session.create_session()
    all_users = session.query(WeatherNotifications).all()
    print(all_users)


if __name__ == '__main__':
    db_session.global_init('db/user.sqlite')  # инициализируем БД
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
    #  запускаем бота
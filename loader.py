from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import TOKEN


storage = MemoryStorage()  #  делаем хранилище для хлама
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)  #  создаём экземпляр бота
dp = Dispatcher(bot, storage=storage)  #  делаем парсер
scheduler = AsyncIOScheduler()  #  создаём планировщик

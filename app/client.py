from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from app.database.requests import set_user


client = Router()




@client.message(CommandStart)
async def cmd_start(massage:Message):
    is_user = await set_user(massage.from_user.id)
    if not is_user:
        await massage.answer('Добро пожаловать! \n Пройдите процесс регистрации...\n\nВведите ваше имя')
    else:
        await massage.answer('Добро пожаловать в наш магазин\n Используйте кнопки ниже')



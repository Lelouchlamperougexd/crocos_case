from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    button = types.KeyboardButton(text = "Отправить свою геолокацию", request_location=True)
    keyboard = types.ReplyKeyboardMarkup(keyboard= [[button]], one_time_keyboard=True)
    await message.answer("Привет! Я помогу тебе построить маршрут по городу для начала работы предоставь доступ к геолокации.", reply_markup = keyboard)

@router.message()
async def handle_text_message(message: types.Message):
    if message.location is not None:
        await handle_location(message)

async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await message.answer(reply)
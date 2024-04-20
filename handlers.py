import sqlite3
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

def get_location_keyboard():
    button = types.KeyboardButton(text = "Отправить свою геолокацию", request_location=True)
    keyboard = types.ReplyKeyboardMarkup(keyboard= [[button]], one_time_keyboard=True, resize_keyboard=True)
    return keyboard

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я помогу тебе построить маршрут по городу для начала работы предоставь доступ к геолокации.", reply_markup = get_location_keyboard())

@router.message()
async def handle_text_message(message: types.Message):
    if message.location is not None:
        await handle_location(message)

async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    with  sqlite3.connect('db.sqlite') as connection :
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE telegram_id = {message.from_user.id}")
        if cursor.fetchone() is None:
            cursor.execute(f"INSERT INTO users VALUES ({message.from_user.id}, '{lat}', '{lon}')")
        else:
            cursor.execute(f"UPDATE users SET lat = {lat}, long = {lon} WHERE telegram_id = {message.from_user.id}")
        connection.commit()
        cursor.close()
    reply = "Теперь вы можете..."
    await message.answer(reply)
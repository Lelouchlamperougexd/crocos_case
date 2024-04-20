import sqlite3
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

def get_standart_keyboard():
    keyboard = types.ReplyKeyboardMarkup(keyboard = [[
        types.KeyboardButton(text = "Отправить свою геолокацию", request_location=True),
        types.KeyboardButton(text = "Получить информацию"),
    ]])
    return keyboard

@router.message(Command("start"))
async def start(message: Message):
    reply = "Привет!"
    await message.answer(reply, reply_markup = get_standart_keyboard())


@router.message(F.text == "Получить информацию")
async def handle_preferences(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard = [[
        types.KeyboardButton(text = "О мероприятиях"),
        types.KeyboardButton(text = "О достопримечательностях"),
        types.KeyboardButton(text = "Об экскурсиях"),
    ]])
    await message.answer("О чём вы хотите получить информацию", reply_markup = keyboard)


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
    reply = "Какой то ответ"
    await message.answer(reply, reply_markup=get_standart_keyboard())
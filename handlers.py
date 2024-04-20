import sqlite3
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import config
import utils
from aiogram import flags
from aiogram.fsm.context import FSMContext

router = Router()

def get_standard_keyboard():
    keyboard = types.ReplyKeyboardMarkup(keyboard = [[
        types.KeyboardButton(text = "Отправить свою геолокацию", request_location=True),
        types.KeyboardButton(text = "Построить маршрут"),
        types.KeyboardButton(text = "Получить информацию о достопремичательностях"),
    ]], resize_keyboard=True, is_persistent=True)
    return keyboard

@router.message(Command("start"))
async def start(message: Message):
    reply = "Привет!"
    await message.answer(reply, reply_markup = get_standard_keyboard())


@router.message(F.text == "Получить информацию о достопремичательностях")
async def handle_preferences(message: types.Message):
    buttons = []
    with  sqlite3.connect('db.sqlite') as connection :
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM places")
        names = cursor.fetchall()
        print(names)
        for name in names:
            buttons.append(types.KeyboardButton(text = name[0]))
        cursor.close()
    if names == []:
        await message.answer("Нет информации о достопремичательностях", reply_markup=get_standard_keyboard())
    else:
        await message.answer("Информация о достопремичательностях", reply_markup = types.ReplyKeyboardMarkup(keyboard=[buttons], one_time_keyboard=True))


@router.message()
async def handle_text_message(message: types.Message):
    if message.location is not None:
        await handle_location(message)
    else:
        response = await utils.generate_text(message.text)
        await message.answer(response, reply_markup=get_standard_keyboard())

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
    await message.answer(reply, reply_markup=get_standard_keyboard())
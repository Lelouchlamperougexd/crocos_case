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

    names = []
    data = []
    with  sqlite3.connect('db.sqlite') as connection :
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM places")
        data = cursor.fetchall()
        for i in data:
            names.append(i[0])
        cursor.close()
    if (message.text in names):
        place_ind = names.index(message.text)
        place = data[place_ind]
        reply = f"""
🏷Название: 
{place[0] if place[0] != 'None' else "Нет данных"}

💬Описание: 
{place[1] if place[1] != 'None' else "Нет данных"}

📝Историческое и культурное значнеие: 
{place[2] if place[2] != 'None' else "Нет данных"}

💵Прайслист:
{place[3] if place[3] != 'None' else "Нет данных"}

🕔Время работы: {place[4] if place[4] != 'None' else "Нет данных" }-{place[5] if place[5] != 'None' else "Нет данных"}

🗺Адрес: {place[6] if place[6] != 'None' else "Нет данных"}

📞Телефон: {place[7] if place[7] != 'None' else "Нет данных"}

🚍Как добраться: {place[8] if place[8] != 'None' else "Нет данных"}
https://maps.google.com/maps?q={place[0].replace(" ", "+").replace("»", "").replace("«", "").replace("<<", "").replace(">>", "")}
"""
        await message.answer(reply, reply_markup = get_standard_keyboard())
        return
    
    response, _ = await utils.generate_text(message.text)
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
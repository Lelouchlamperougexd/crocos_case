import sqlite3
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import config
router = Router()

def get_standart_keyboard():
    keyboard = types.ReplyKeyboardMarkup(keyboard = [[
        types.KeyboardButton(text = "Отправить свою геолокацию", request_location=True),
        types.KeyboardButton(text = "Построить маршрут"),
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

openai.api_key = config.openai_api_key

async def handle_question(message: types.Message):
    question = message.text
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            temperature=0.5,
            max_tokens=100
        )
        answer = response.choices[0].text.strip()
        await message.answer(answer, reply_markup=get_standard_keyboard())
    except Exception as e:
        await message.answer("Извините, возникла ошибка при обработке запроса.", reply_markup=get_standard_keyboard())


@router.message(F.text == "О мероприятиях")
async def handle_preferences(message: types.Message):
    await message.answer("Информация о мероприятиях", reply_markup = get_standart_keyboard())

@router.message(F.text == "О достопримечательностях")
async def handle_preferences(message: types.Message):
    await message.answer("Информация о достопремичательностях", reply_markup = get_standart_keyboard())

@router.message(F.text == "Об экскурсиях")
async def handle_preferences(message: types.Message):
    await message.answer("Информация об экскурсиях", reply_markup = get_standart_keyboard())

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
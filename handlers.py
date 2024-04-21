import sqlite3
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import config
import utils
from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import places
import asyncio
from typing import List
import datetime


router = Router()

class ConstructPath(StatesGroup):
    places = State()
    travel_mode = State()
    location = State()

async def cancel_operation(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.clear()

    await message.reply('Вы отменили своё действие.', reply_markup=get_standard_keyboard())

def get_standard_keyboard(state: State = None):
    buttons = [
        types.KeyboardButton(text = "Построить маршрут"),
        types.KeyboardButton(text = "Получить информацию о достопримечательностях"),
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard = [buttons], resize_keyboard=True, is_persistent=True)
    return keyboard

@router.message(Command("start"))
async def start(message: Message):
    reply = f"Здравствуйте, {message.from_user.first_name}! Чем могу быть полезен?"
    await message.answer(reply, reply_markup = get_standard_keyboard())


@router.message(F.text == "Получить информацию о достопримечательностях")
async def handle_preferences(message: types.Message):
    buttons = []
    for place in places.places():
        buttons.append(types.KeyboardButton(text = place.name))
    if places.places() == []:
        await message.answer("Нет информации о достопримечательностях", reply_markup=get_standard_keyboard())
    else:
        await message.answer("Выберите информацию о достопримечательности которая вам интересна", reply_markup = types.ReplyKeyboardMarkup(keyboard=[buttons], one_time_keyboard=True))


@router.message(F.text == "Построить маршрут")
async def handle_preferences(message: types.Message, state: FSMContext):
    text = """
Выберите интересующие вас достопримечательности (Отправте номера интересующих достопримечательностей через пробел):
"""
    for i,val in enumerate(places.places()):
        text+= f"{i}) {val.name}\n"
    await state.set_state(ConstructPath.places)
    buttons = [types.KeyboardButton(text = "Отменить"),]
    keyboard = types.ReplyKeyboardMarkup(keyboard = [buttons], resize_keyboard=True)
    await message.answer(text, reply_markup=keyboard)


@router.message(ConstructPath.places)
async def handle_preferences_place(message: types.Message, state: FSMContext):
    if (await state.get_state() == None):
        return
    if (message.text == "Отменить"):
        await cancel_operation(message, state)
        return
    place_indexes = [int(i) for i in message.text.split()]
    await state.update_data(places = [val for i,val in enumerate(places.places()) if i in place_indexes])
    buttons = [types.KeyboardButton(text = "Отменить"),]
    keyboard = types.ReplyKeyboardMarkup(keyboard = [buttons], resize_keyboard=True)
    await message.answer("""Теперь выберите способ передвижения
0) На машине
1) Пешком
2) На велосипеде
3) На общественном транспорте
""", reply_markup=keyboard)
    await state.set_state(ConstructPath.travel_mode)

@router.message(ConstructPath.travel_mode)
async def handle_travel_mode(message: types.Message, state: FSMContext):
    if (await state.get_state() == None):
        return
    if (message.text == "Отменить"):
        await cancel_operation(message, state)
        return
    mode = ("driving","walking","bicycling","transit")[int(message.text)]
    await state.update_data(travel_mode = mode)
    buttons = [
        types.KeyboardButton(text = "Отменить"),
        types.KeyboardButton(text = "Отправить свою геолокацию", request_location=True),
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard = [buttons], resize_keyboard=True)
    await message.answer("Теперь нужно дать доступ к местоположению", reply_markup=keyboard)
    await state.set_state(ConstructPath.location)

@router.message(ConstructPath.location)
async def handle_travel_mode(message: types.Message, state: FSMContext):
    if (await state.get_state() == None):
        return
    if (message.text == "Отменить"):
        await cancel_operation(message, state)
        return
    await state.update_data(location = message.location)
    path = await build_path(message, state)
    data = await state.get_data()
    if (len(path[0][1:]) == 0) :
        reply = "Извините, но все достопримечательности в данный момент закрыты"
        await message.answer(reply, reply_markup=get_standard_keyboard())
        await state.clear()
        return
    if len(path[0][1:]) < len(data['places']):
        reply = """
Вот в каком порядке вам следует пройтись по достопримечательностям(к сожелению остальные выбранные достопримечательности вы не успеете пройти):
"""
    else:
        reply = """
Вот в каком порядке вам следует пройтись по достопримечательностям:
"""
    for i,val in enumerate(path[0][1:]):
        reply+=f"{i+1}) {val.name}\n"
    await message.answer(reply, reply_markup=get_standard_keyboard())
    await state.clear()

async def build_path(message: Message, state: FSMContext):
    data = await state.get_data()
    lat = data['location'].latitude
    lon = data['location'].longitude
    best_path = await build_path_rec([places.Place(address=f"{lat},{lon}")], data['places'], data['travel_mode'])
    return best_path

async def build_path_rec(current_path: List[places.Place], places_left: List[places.Place], mode: str, time: int = 0):
    best_path = (None, -1)
    if (len(places_left) == 0):
        return (current_path, time)
    for i in range(len(places_left)):
        opens = [int(i) for i in places_left[i].start.split(":")]
        closes = [int(i) for i in places_left[i].end.split(":")]
        opens = datetime.time(opens[0], opens[1])
        closes = datetime.time(closes[0], closes[1])
        opens = datetime.datetime.combine(datetime.datetime.now(), opens)
        closes = datetime.datetime.combine(datetime.datetime.now(), closes)
        current_time = datetime.datetime.now() + datetime.timedelta(seconds=time)
        if (opens <= current_time <= closes):
            time_to = (await utils.fetch_from_google(current_path[-1].address, places_left[i].address, mode))['routes'][0]['legs'][0]['duration']['value']
            path = await build_path_rec(current_path + [places_left[i]], places_left[:i]+places_left[i+1:], mode, time+time_to)
            if best_path[1] == -1 or best_path[1] > path[1]:
                best_path = path
    if best_path[1] == -1 or len(best_path[0]) < len(current_path):
        best_path = (current_path, time)
        
    return best_path

    
@router.message()
async def handle_text_message(message: types.Message):
    names = []
    for i in places.places():
        names.append(i.name)
    if (message.text in names):
        place_ind = names.index(message.text)
        place: places.Place = places.places()[place_ind]
        reply = f"""
🏷Название: 
{place.name}

💬Описание: 
{place.description}

📝Историческое и культурное значнеие: 
{place.value}

💵Прайслист:
{place.price}

🕔Время работы: {place.start}-{place.end}

🗺Адрес: {place.address}

📞Телефон: {place.phone}

🚍Как добраться: {place.transport}
{place.url}"""
        
        await message.answer(reply, reply_markup = get_standard_keyboard())
        return
    
    #response = await utils.generate_text(message.text)
    #await message.answer(response, reply_markup=get_standard_keyboard())
    
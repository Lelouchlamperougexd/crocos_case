import asyncio
import logging
import sqlite3

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router

import config

from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    text_prompt = State()

async def main():
    with  sqlite3.connect('db.sqlite') as connection :
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS places (name VARCHAR, description VARCHAR, value VARCHAR, price VARCHAR, start TEXT, end TEXT, address VARCHAR, phone VARCHAR, transport VARCHAR)")
        connection.commit()

        cursor.close()
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
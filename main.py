# Тестовый телеграм эхо бот, запщенный на сервере с гитхаба
# Тестовый комит
# для aiogram pip install aiogram==2.25.2

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode #       -- содержит настройки разметки сообщений (HTML, Markdown)
from aiogram.fsm.storage.memory import MemoryStorage # -- хранилища данных для состояний пользователей

from handlers import router # type: ignore 


# def read_data (sFile_data):
# 	global API_TOKEN
# 	pFile_data = open (sFile_data, "r")
# 	API_TOKEN = pFile_data.readline ()
# 	return 0
# read_data ("data.txt")

# Удалено чтение токена из айла, пока хз почему не работает
API_TOKEN = input ()




async def main():
    bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
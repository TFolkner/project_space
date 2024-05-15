# Тестовый телеграм эхо бот, запщенный на сервере с гитхаба
# Тестовый комит
# для aiogram pip install aiogram==2.25.2

import asyncio
import logging

from aiogram import Bot, Dispatcher # type: ignore 
from aiogram.enums.parse_mode import ParseMode # type: ignore 
from aiogram.fsm.storage.memory import MemoryStorage # type: ignore 

import config # type: ignore 
from handlers import router # type: ignore 





def read_data (sFile_data):
	global API_TOKEN
	pFile_data = open (sFile_data, "r")
	API_TOKEN = pFile_data.readline ()
	return 0





def main ():
	read_data ("data.txt")
	return 0


if __name__ == '__main__':
	main()
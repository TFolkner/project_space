# from aiogram import types, F, Router
# from aiogram.types import Message
# from aiogram.filters import Command

# router = Router()




# @router.message(Command("help"))
# async def message_to_any (msg:Message):
#     await msg.answer ("Доступные комманды:\n" +
#                       "/help  - хелп, он и в Африке Хэлп\n" +
#                       "/hello - приветственное сообщение\n" +
#                       "/ID    - узнать твой ID")


# @router.message(Command("hello"))
# async def message_hello (msg:Message):
#     await msg.answer("Привет!\n" +
#                      "Я быстроразвивающийся бот проекта \"КОСМОС\".\n" +
#                      "Мой функционал пока сильно ограничен, но скоро я буду умнее.\n" +
#                      "Рад знакомству с тобой.")


# @router.message(Command("ID"))
# async def message_handler(msg: Message):
#     await msg.answer(f"Твой ID: {msg.from_user.id}")


# @router.message()
# async def message_to_any (msg:Message):
#     await msg.answer ("Неизвестная комманда\n"+
#                       "используй /help")

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
# @router.message()

async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

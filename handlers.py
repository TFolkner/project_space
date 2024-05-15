from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()




@router.message(Command("help"))
async def message_to_any (msg:Message):
    await msg.answer ("Доступные комманды:\n" +
                      "/help  - хелп, он и в Африке Хэлп\n" +
                      "/hello - приветственное сообщение\n" +
                      "/ID    - узнать твой ID")


@router.message(Command("hello"))
async def message_hello (msg:Message):
    await msg.answer("Привет!\n" +
                     "Я быстроразвивающийся бот проекта \"КОСМОС\".\n" +
                     "Мой функционал пока сильно ограничен, но скоро я буду умнее.\n" +
                     "Рад знакомству с тобой.")


@router.message(Command("ID"))
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")


@router.message()
async def message_to_any (msg:Message):
    await msg.answer ("Неизвестная комманда\n"+
                      "используй /help")
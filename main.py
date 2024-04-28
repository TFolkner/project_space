# Тестовый телеграм эхо бот, запщенный на сервере с гитхаба


from aiogram import Bot, Dispatcher, types, executor
# для aiogram pip install aiogram==2.25.2


API_TOKEN = '7061565788:AAG-e1jFINrhKbBLoXs5Pg_YJokM634j740'
bot = Bot (token = API_TOKEN)
dp = Dispatcher (bot)


@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем. 
async def send_welcome(message: types.Message):
   await message.reply("Привет,я тестовый бот проекта \"КОСМОС\"\n Тут будут тестироваться новые функции, приятного использования\n :-)") 
   #Так как код работает асинхронно, то обязательно пишем await.


#Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
@dp.message_handler() 
async def echo(message: types.Message): 
   #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
   await message.answer(message.text)



if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
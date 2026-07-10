import os
from aiogram import Bot, Dispatcher, executor

# هذا السطر يخلي البوت يسحب التوكن من Railway وليس من الكود
API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("أبشر يا محمد، البوت شغال!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

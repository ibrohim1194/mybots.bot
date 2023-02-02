import logging
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN

logging.basicConfig(level=logging.INFO)



bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



# Start buyrug'ini ishlatish
@dp.message_handler(commands=['satrt'])
async def start(message: types.Message):
    await message.answer('Assalomu alaykum')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 
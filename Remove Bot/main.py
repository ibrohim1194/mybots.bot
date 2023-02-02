import logging 
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
from aiogram.types import ContentType,Message
from pathlib import  Path
import requests
from kod import to_cyrillic, to_latin



# logging
logging.basicConfig(level=logging.INFO)




# Bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



# Start command
@dp.message_handler(commands="start")
async def start(message: types.Message):
    ism = message.from_user.first_name
    await message.answer(f"Hello {ism}, welcom to the Bot")


@dp.message_handler(commands="help")
async def help(message: types.Message):
    await message.answer("Latin - Cirilic")







@dp.message_handler()
async def latini(message: types.Message):
    if message == to_cyrillic:
        await message.answer(to_latin)
    elif message == to_latin:
        await message.answer(to_cyrillic)

























# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
import json
from config import API_TOKEN

app_id = "762535f5"
app_key = "dc86b6aa51a998ea8284880e6ffc98f4"

language = "en-gb"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    ism = message.from_user.first_name
    await message.reply(f"Assalomu aleykum {ism}. Dictionary botimizga xush kelibsiz.\nKerakli so'zni kiriting👇🏻:")



@dp.message_handler()
async def echo(message: types.Message):
    try:
        word_id = message.text
        url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
        r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
        natija = r.json()
        audio1 = natija['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
        definition = natija['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']
        await message.answer(definition)
        await message.answer(audio1)
    except:
        await message.answer("Notog'ri so'z kiritildi.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



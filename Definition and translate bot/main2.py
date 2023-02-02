import logging
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator

API_TOKEN = '5967641723:AAGaOm5wd6fdxlyWrJud3mJrwQQsJQOPnjI'
translator = Translator()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_welcome(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split())>2:
        dest = "uz" if lang == "en" else 'en'
    await message.reply(translator.translate(message.text, dest).text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
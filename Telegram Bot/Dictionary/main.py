# import requests
# from aiogram.types import Message
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher import Dispatcher
# from aiogram import Bot, types
# from aiogram import executor

# class TranslateBot(StatesGroup):
#     word_to_translate = State()
#     translation = State()

# # Initialize the bot and dispatcher
# API_TOKEN = '5539952146:AAFefsZfm4R0Ti3bNplbipHjoIFW0Q9sPNE'
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)




# # @dp.message_handler(commands=["start"])
# # async def start(message: types.Message):
# #     await message.answer('Assalomu alykum Botimizga xush kelibsiz!')

# # @dp.message_handler(commands=["help"])
# # async def start(message: types.Message):
# #     await message.answer("Biror o'zingizga kerakli so'zni kiriting ")

# # @dp.message_handler(commands=["admin"])
# # async def start(message: types.Message):
# #     await message.answer("Admin bilan bog'lanish uchun @ibrohim1194 akkauntiga murojat qiling!")






# # Register the states with the dispatcher
# # dp.register_message_handler(TranslateBot.word_to_translate, text="translate")
# # dp.register_message_handler(TranslateBot.translation, text="translate", state=TranslateBot.word_to_translate)

# # @dp.message_handler(state=TranslateBot.word_to_translate)
# # async def ask_word(message: types.Message, state: FSMContext):
# #     await message.answer("Qaysi so'zni tarjima qilishni hohlaysiz?")
# #     await TranslateBot.next()

# # @dp.message_handler(state=TranslateBot.translation)
# # async def translate_word(message: types.Message, state: FSMContext):
# #     # Get the word from the user
# #     word = message.text
# #     # Use the Oxford Dictionary API to translate the word
# #     app_id = 'YOUR_APP_ID'
# #     app_key = 'YOUR_APP_KEY'
# #     url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/en-gb/' + word.lower()
# #     r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
# #     # Get the translation from the API response
# #     if r.status_code == 200:
# #         json_data = r.json()
# #         translation = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
# #         await message.answer(translation)
# #     else:
# #         await message.answer("Sorry, I couldn't find a translation for that word.")
# #     await state.finish()

# if __name__ == '__main__':
#     executor.start_polling(dp,skip_updates=True)



import logging
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
from googletrans import Translator

API_TOKEN = "5539952146:AAFefsZfm4R0Ti3bNplbipHjoIFW0Q9sPNE"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


translator = Translator()




@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Assalomu alaykum!")
    
@dp.message_handler(commands=["help"])
async def start(message: types.Message):
    await message.answer("Tarjim aqilishni xoxlagan so'zingizni kiriting.")

@dp.message_handler(commands=["admin"])
async def start(message: types.Message):
    await message.answer("Admin bilan bog'lanish uchun @ibrohim1194 akkauntiga murojat qiling.")


@dp.message_handler()
async def echo(message:types.Message):
    javob = translator.translate(message.text, dest='uz')
    await message.answer(javob.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
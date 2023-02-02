import logging
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
from tugmalar  import natija


# logging qismi
logging.basicConfig(level=logging.INFO)


# Botni ulash qismi
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



# Start command
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    ism = message.from_user.first_name
    await message.answer(f"Assalomu alaykum {ism} Botga xush kelibsiz",reply_markup=natija)


@dp.message_handler()
async def buttons(message: types.Message):
    if message.text == "O'zbek tili🇺🇿":
        await message.answer("Siz O'bek tilini tanladingiz")
    elif message.text == "Русский🇷🇺":
        await message.answer("Вы выбрали Русский язык")
    elif message.text == "English🇺🇸":
        await message.answer("You have selected English")








# start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
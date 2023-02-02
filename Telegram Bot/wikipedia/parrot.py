import logging
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN1
import wikipedia as wk



# Loggingni sozlamasi
logging.basicConfig(level=logging.INFO)


wk.set_lang("uz")

# Front-End bilan Back-End ni bog'lash qismmi

bot = Bot(token=API_TOKEN1)
dp = Dispatcher(bot)









# Start buyrug'ini ishlatish qismi
@dp.message_handler(commands=["start"])
async def start(message: types.Message): # agar bu yerda "async" buyrug'i ishlatilmasa botni 1-odam ishlatib bolgandan keyin boshqa odam ishlatadi.
    await message.answer("Assalomu alaykum! Botimizga xush kelibsiz!")



# Admin buyrug'ini ishlatish qismi
@dp.message_handler(commands=["admin"])
async def start(message: types.Message): # agar bu yerda "async" buyrug'i ishlatilmasa botni 1-odam ishlatib bolgandan keyin boshqa odam ishlatadi.
    await message.answer("Admin bilan bog'lanish uchun +998999111194 raqamiga murojat qiling.")


# Help buyrug'ini ishlatish qismi
@dp.message_handler(commands=["help"])
async def start(message: types.Message): # agar bu yerda "async" buyrug'i ishlatilmasa botni 1-odam ishlatib bolgandan keyin boshqa odam ishlatadi.
    await message.answer("Bu Bot siz nima yozsangiz o'sha narsani sizga qaytaradi.")




# Echo Bot (takrorlovchi bot)
@dp.message_handler()
async def start(message:types.Message):
    await message.answer(message.text)








# Botni ishga tushirish qismi

if __name__ == "__main__":# Agar faylning nomi "main"ga teng bolsa bot ishga tushsin    
    executor.start_polling(dp,skip_updates=True)

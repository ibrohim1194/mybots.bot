import logging
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
import wikipedia as wk



# Loggingni sozlamasi
logging.basicConfig(level=logging.INFO)


wk.set_lang("uz")

# Front-End bilan Back-End ni bog'lash qismmi

bot = Bot(token=API_TOKEN)
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
    await message.answer("Sizga kerak bo'lgan narsa nomini kiriting yoki @ibrohim1194 akkauntiga murojat qiling.")




# Wikipedia Bot (Takrorlovchi Bot)
@dp.message_handler()
async def start(message: types.Message):
    ab = wk.summary(message.text)
    await message.answer(ab)


# Echo,Bot (takrorlovchi bot)
# @dp.message_handler()
# async def sendwiki(message:types.message):
#     try:
#       natija = wk.summary(message.text)
#       await message.answer(natija)
#     except:
#         await message.answer("Topilmadi!")





# Botni ishga tushirish qismi

if __name__ == "__main__":# Agar faylning nomi "main"ga teng bolsa bot ishga tushsin    
    executor.start_polling(dp,skip_updates=True)

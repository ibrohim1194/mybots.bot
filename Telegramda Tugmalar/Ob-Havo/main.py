import logging 
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
from tugmalar import natija, natija2
import requests
from bs4 import BeautifulSoup


# Logging sozlamasi
logging.basicConfig(level=logging.INFO)


# Botni ulash qismi
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)





# result = ""
# def func():
#     global result
#     shahar = input.get()
#     url = f"https://obhavo.uz/{shahar}"
#     us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

  

#     toliq_sayt = requests.get(url, headers=us)
#     malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')

#     malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
#     natija = malumot_olish[0].text
#     text1.insert('1.0',natija)






# Start buyrug'i
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ism = message.from_user.first_name
    await message.answer(f"Assalomu alaykum {ism} botimizga xush kelibsiz", reply_markup=natija)












@dp.callback_query_handler(lambda b: b.data == "uz")
async def uzbek(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Siz o'zbek tilini tanladingiz", reply_markup=natija2)


@dp.message_handler()
async def tashkent(message: types.Message):
    if message.text == 'tashkent':
        tashkent = 'tashkent'
        url = f"https://obhavo.uz/{tashkent}"
        
        us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        toliq_sayt = requests.get(url, headers=us)
        malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')

        malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
        javob = malumot_olish[0].text
        await message.answer("Ertalab:\nKechqurun",javob)




    elif message.text == 'samarkand':
        samarkand = 'samarkand'
        url = f"https://obhavo.uz/{samarkand}"
    
        us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        toliq_sayt = requests.get(url, headers=us)
        malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')
        malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
        javob = malumot_olish[0].text
        await message.answer(javob)


    elif message.text == 'bukhara':
        bukhara = 'bukhara'
        url = f"https://obhavo.uz/{bukhara}"
    
        us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        toliq_sayt = requests.get(url, headers=us)
        malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')
        malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
        javob = malumot_olish[0].text
        await message.answer(javob)



    elif message.text == 'khiva':
        khiva = 'khiva'
        url = f"https://obhavo.uz/{khiva}"
    
        us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        toliq_sayt = requests.get(url, headers=us)
        malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')
        malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
        javob = malumot_olish[0].text
        await message.answer(javob)



    elif message.text == 'ferghana':
        ferghana = 'ferghana'
        url = f"https://obhavo.uz/{ferghana}"
    
        us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        toliq_sayt = requests.get(url, headers=us)
        malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')
        malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
        javob = malumot_olish[0].text
        await message.answer(javob)




    elif message.text == 'andijan':
        andijan = 'andijan'
        url = f"https://obhavo.uz/{andijan}"
    
        us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        toliq_sayt = requests.get(url, headers=us)
        malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')
        malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
        javob = malumot_olish[0].text
        await message.answer(javob)




    elif message.text == 'namangan':
        namangan = 'namangan'
        url = f"https://obhavo.uz/{namangan}"
    
        us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        toliq_sayt = requests.get(url, headers=us)
        malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')
        malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
        javob = malumot_olish[0].text
        await message.answer(javob)



    elif message.text == 'jizzakh':
        jizzakh = 'jizzakh'
        url = f"https://obhavo.uz/{jizzakh}"
    
        us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        toliq_sayt = requests.get(url, headers=us)
        malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')
        malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
        javob = malumot_olish[0].text
        await message.answer(javob)



    elif message.text == 'navoi':
        navoi = 'navoi'
        url = f"https://obhavo.uz/{navoi}"
    
        us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        toliq_sayt = requests.get(url, headers=us)
        malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')
        malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
        javob = malumot_olish[0].text
        await message.answer(javob)


































if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
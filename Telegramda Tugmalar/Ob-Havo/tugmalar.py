from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton,InlineKeyboardMarkup


# ichki tugma
uz = InlineKeyboardButton(text="O'zbek tili🇺🇿",callback_data="uz")
ru = InlineKeyboardButton(text="Русский🇷🇺",callback_data="ru")
us = InlineKeyboardButton(text="English🇺🇸",callback_data="us")

natija = InlineKeyboardMarkup().add(uz,ru,us)




toshkent = KeyboardButton(text='tashkent')
samarqand = KeyboardButton('samarkand')
buxoro = KeyboardButton(text='bukhara')
xiva = KeyboardButton(text='khiva')
fargona = KeyboardButton(text='ferghana')
andijon = KeyboardButton(text='andijan')
namangan = KeyboardButton(text='namangan')
jizzax = KeyboardButton(text='jizzakh')
navoiy = KeyboardButton(text='navoi')



natija2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(toshkent,samarqand,buxoro).add(xiva,fargona,andijon).add(namangan,jizzax,navoiy)
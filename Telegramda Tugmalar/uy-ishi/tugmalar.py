from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton,InlineKeyboardMarkup



# Languages
uzbek = KeyboardButton(text="O'zbek tili🇺🇿")
russian = KeyboardButton(text="Русский🇷🇺")
eng = KeyboardButton(text="English🇺🇸")

natija = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(uzbek,russian).add(eng)




# ichki tugma
# uz = InlineKeyboardButton(text="O'zbek tili🇺🇿",callback_data="uz")
# ru = InlineKeyboardButton(text="Русский🇷🇺",callback_data="ru")
# us = InlineKeyboardButton(text="English🇺🇸",callback_data="us")

# natija = InlineKeyboardMarkup().add(uz,ru,us)




info = KeyboardButton(text="Ma'lumot")
contact = KeyboardButton(text="Telefon raqam",request_contact=True)
location = KeyboardButton(text="Lokatsiya",)#request_location=True
courses = KeyboardButton(text="Kurslar")
tel = KeyboardButton(text="Telefon raqam")
joy = KeyboardButton(text="Joylashuv")


natija2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(info).row(contact,location).add(courses).add(tel,joy)




info3 = KeyboardButton(text="Информация")
contact3 = KeyboardButton(text="Отправить номер телефона",request_contact=True)
location3 = KeyboardButton(text="Отправить местоположение",request_location=True)
courses3 = KeyboardButton(text="Курсы")
tel3 = KeyboardButton(text="Номер телефона")

natija3 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(info3).row(contact3,location3).add(courses3).add(tel3)




info4 = KeyboardButton(text="Information")
contact4 = KeyboardButton(text="Send phone number",request_contact=True)
location4 = KeyboardButton(text="Send location",request_location=True)
courses4 = KeyboardButton(text="Courses")
tel4 = KeyboardButton(text="Phone Number")


natija4 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(info4).row(contact4,location4).add(courses4).add(tel4)








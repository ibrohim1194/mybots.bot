from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup



# Languages
# uzbek = KeyboardButton(text="O'zbek tili🇺🇿")
# russian = KeyboardButton(text="Русский🇷🇺")
# eng = KeyboardButton(text="English🇺🇸")


# # main page buttons
# info = KeyboardButton(text="Ma'lumot")
# contact = KeyboardButton(text="Telefon raqamni yuborish",request_contact=True)
# location = KeyboardButton(text="Lokatsiya yuborish",request_location=True)
# courses = KeyboardButton(text="Kurslar")

# natija2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(info).row(contact,location).add(courses)





# natija = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(uzbek,russian).add(eng)
# # natija = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(uzbek,russian,eng)




# inline keyboard
uz = InlineKeyboardButton(text="O'zbek tili🇺🇿",callback_data="uz")
ru = InlineKeyboardButton(text="Русский🇷🇺",callback_data="ru")
us = InlineKeyboardButton(text="English🇺🇸",callback_data="us")
link = InlineKeyboardButton(text='Saytga kirish', url="https://marsit.uz/")
sin = InlineKeyboardButton(text='Botni taklif qilish', switch_inline_query='S1mple')
sin2 = InlineKeyboardButton(text='Hozirgi chatga habar yuborish', switch_inline_query_current_chat='S1mple')

natija = InlineKeyboardMarkup().add(uz,ru,us).add(link).add(sin).add(sin2)
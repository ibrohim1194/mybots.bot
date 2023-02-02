from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton,InlineKeyboardMarkup



uz = KeyboardButton(text="O'zbek tili🇺🇿")
ru = KeyboardButton(text="Русский🇷🇺")

natija = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(uz,ru)




back = KeyboardButton(text="Orqaga↩️")


natija3 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(back)




malumot = KeyboardButton(text="Ma'lumot📋")
malumot2 = KeyboardButton(text="Xodimlar haqida ma'lumot🤵")
yordam = KeyboardButton(text="Nima yordam bera olaman😇")
savol = KeyboardButton(text="Savollar❔")
til = KeyboardButton(text="Tilni o'zgartirish🇷🇺")


natija2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(malumot).add(malumot2).add(yordam).add(savol,til).add(back)










# xodimlar
mudir = KeyboardButton(text="Bolim mudiri🤵🏼‍♂️")
doctor = KeyboardButton(text="Doktor👨‍⚕️")
psixolog = KeyboardButton(text="Psixolog👩‍⚕️")
ijtimoiy = KeyboardButton(text="Ijtimoiy xodim🧑🏻‍💼")

xodimlar = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(mudir,doctor).add(psixolog,ijtimoiy).add(back)






# yordam
pul = KeyboardButton(text="Pul Yordami💸")

oyinchoq = KeyboardButton(text="O'yinchoq🧸")
kongilli = KeyboardButton(text="Ko'ngilli bo'lmoqchiman🙋‍♂️")

oziq = KeyboardButton(text="Oziq-Ovqat🍕")
boshqa = KeyboardButton(text="Boshqa🧐")

yordam = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(pul).add(oyinchoq,kongilli).add(oziq,boshqa).add(back)



click = KeyboardButton(text="Click💳")
payme = KeyboardButton(text="PayMe💳")

karta_t = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(click,payme).add(back)
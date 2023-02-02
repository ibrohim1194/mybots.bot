import logging
from aiogram import Bot, Dispatcher,executor,types
from config import API_TOKEN
from tugmalar import natija, natija2, xodimlar, natija3, yordam, karta_t







# logging
logging.basicConfig(level=logging.INFO)




bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    ism = message.from_user.first_name
    await message.answer(f"Salom! {ism}",reply_markup=natija)





@dp.message_handler()
async def tugmalar(message: types.Message):
    if message.text == "O'zbek tili🇺🇿":
        await message.answer("Siz O'zbek tilini tanladingiz!",reply_markup=natija2)
    elif message.text == "Ma'lumot📋":
        await message.answer_photo("https://www.gazeta.uz/media/img/2022/08/PC8GeB16617013146873_l.jpg",
        caption="Taskin",reply_markup=natija3)
    elif message.text == "Xodimlar haqida ma'lumot🤵":
        await message.answer("Xodimlarni tanlang:",reply_markup=xodimlar)
    elif message.text == "Orqaga↩️":
        await message.answer("Orqaga qaytish",reply_markup=natija2)
    elif message.text == "Tilni o'zgartirish🇷🇺":
        await message.answer("Tilni tanlang",reply_markup=natija)

    # Ishchilar
    elif message.text == "Bolim mudiri🤵🏼‍♂️":
        await message.answer_photo("https://thumbs.dreamstime.com/b/business-man-standing-confident-smile-portrait-successful-suit-smiling-proud-outdoors-44304293.jpg",
        caption="Bolim mudiri: Avazbek Odilov")
    elif message.text == "Doktor👨‍⚕️":
        await message.answer_photo("https://hips.hearstapps.com/hmg-prod/images/portrait-of-a-happy-young-doctor-in-his-clinic-royalty-free-image-1661432441.jpg?crop=0.66698xw:1xh;center,top&resize=1200:*",
        caption="Shifokor: Abdurahim Aliyev")
    elif message.text == "Psixolog👩‍⚕️":
        await message.answer_photo("https://strategicpsychology.com.au/wp-content/uploads/Personal-counselor.jpg",
        caption="Aziza To'rayeva")
    elif message.text == "Ijtimoiy xodim🧑🏻‍💼":
        await message.answer_photo("https://t4.ftcdn.net/jpg/02/24/86/95/360_F_224869519_aRaeLneqALfPNBzg0xxMZXghtvBXkfIA.jpg",
        caption="Toxir Asqarov")



    # yordam
    elif message.text == "Nima yordam bera olaman😇":
        await message.answer("Yordamni tanlang:",reply_markup=yordam)
    elif message.text == "Pul Yordami💸":
        await message.answer("Click yoki PayMe",reply_markup=karta_t)
    elif message.text == "Click💳":
        await message.answer("Ushbu kartaga to'lov qilishingiz mumkin:\n123456789123")
    elif message.text == "PayMe💳":
        await message.answer("Ushbu kartaga to'lov qilishingiz mumkin:\n321987654321")




    # savol
    elif message.text == "Savollar❔":
        await message.answer("Savolingizni yozib qoldiring, tez orada biz unga javob yuboramiz.",reply_markup=natija3)
    elif message.text == "O'yinchoq🧸":
        await message.answer("Mumkin bo'lmagan o'yinchoqlar❌.\n👉1. Yumshoq tukli o'yinchoqlar.\n👉2. Sochi bor O'yinchoqlar.\n Mumkin bo'lgan o'yinchoqlar✅.\n👉1. Lego.\n👉2. Birgalikda bo'yaladigan raskraskalar.\n👉3.Tvister\n👉4. Qum (suniy).\n👉5. Kachela ichkariga qo'yiladigan.\n\n☎️ Tel: +99870 202-00-42\n☎️ Tel: +99893 423-00-09")
    elif message.text == "Ko'ngilli bo'lmoqchiman🙋‍♂️":
        await message.answer("Quyidagi link orqali ro'yxatdan o'ting:\nhttps://docs.google.com/forms/d/e/1FAIpQLSd9VLvjxYdBPPEDSS_QbTIvydHbR_BK5nsCj7AnObZiI3knbw/viewform")
    elif message.text == "Oziq-Ovqat🍕":
        await message.answer(
            "Bollar uchun oziq-ovqatlar✅.\n👉1. Yogurt.\n👉2. Kartoshkali pyure.\n👉3. Mevalar(hamma turi).\n👉4. Soklar(katta, kichik).\n👉5. Shirinliklar\n\n☎️ Tel: +99870 202-00-42\n☎️ Tel: +99893 423-00-09"
        )
    elif message.text == "Boshqa🧐":
        await message.answer("👕 Kiyim\n💊 Dori-darmon\n\n☎️ Tel: +99870 202 00 42\n☎️ Tel: +99893 423 00 09\n\n📍 Bizning manzil.👇")
        await message.answer("https://maps.google.com/maps?q=41.173422,69.193470&ll=41.173422,69.193470&z=16")
        await message.answer("Yordam berganingiz uchun raxmat")

    






if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
































# import logging
# from aiogram import Bot,Dispatcher,executor,types
# import requests
# from config import API_TOKEN
# from tugmalar import natija,natija2,natija3


# logging.basicConfig(level=logging.INFO)

# bot=Bot(API_TOKEN)
# dp=Dispatcher(bot)

# @dp.message_handler(commands=["start"]) 
# async def start(message: types.Message):
#     ism=message.from_user.first_name
#     await message.answer(f"Assalomu alekom  {ism}  Botimizga hushkelibsiz",reply_markup=natija)
# @dp.message_handler()
# async def buttons(message: types.Message):
#         if message.text == "O'zbek tili🇺🇿":
#             await message.answer("Siz o'zbek tilini tanladingiz.",reply_markup=natija2)
#         elif message.text == "Rus tili🇷🇺":
#             await message.answer("Вы выбрали русский",reply_markup=natija2)
#         elif message.text == "Ingliz tili🇺🇸":
#             await message.answer("You have selected English",reply_markup=natija2)
#         elif message.text == "Ma'lumot":
#             await message.answer("Bizda o'quv kurslarimiz haftada 3 marotaba boladi",reply_markup=natija3)
#         elif message.text == "Xodimlar haqida malumot🧑‍💻":
#             await message.answer("Bizda asosan erkak xodimlar ishlaydilar!")
#         elif message.text=="Nima yordam bera olaman?":
#             await message.answer("Yordam uchun adminga bog'laning")
#         elif message.text=="Savollar❔":
#             await message.answer_contact("Savollar uchun mars_it  ga bog'laning")
#         elif message.answer("Tilni ozgartirish"):
#             await message.answer("Tilni ozgartirish uchun ortga qayting",reply_markup=natija)
#         elif message.text == "Orqaga":
#             await message.answer(reply_markup=natija2)
        
            


    





# executor.start_polling(dp,skip_updates=True)
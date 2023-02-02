import logging 
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
from tugmalar import natija, natija2, natija3, natija4


# logging sozlamasi
logging.basicConfig(level=logging.INFO)


# Botni ulash qismi
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# start buyrug'i
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ism = message.from_user.first_name
    await message.answer(f"Assalomu alaykum {ism} botimizga xush kelibsiz", reply_markup=natija)




@dp.message_handler()
async def buttons(message: types.Message):
    if message.text == "O'zbek tili🇺🇿":
        await message.answer("Siz O'zbek tilini tanladingiz.",reply_markup=natija2)
    elif message.text == "Русский🇷🇺":
        await message.answer("Вы выбрали Русский язык",reply_markup=natija3)
    elif message.text == "English🇺🇸":
        await message.answer("You have selected English",reply_markup=natija4)
    

    elif message.text == "Ma'lumot":
        await message.answer("Bizning o'quv markaz Chilonzor tumanida Novza Metro yaqinida joylashgan. Bizda malakali o'qituvchilar mavjud. Bizning Onlayn darslarimizni YouTube da ko'rishingiz mumkin")
    elif message.text == "Kurslar":
        await message.answer("Bizning o'quv markazimizda Arab, Ingliz, Rus tillari mavjud. Darslarga ro'yxatdan o'tish uchun +998997630809 raqamiga murojat qiling.")


    elif message.text == "Информация":
        await message.answer("Наш образовательный центр находится в Чиланзарском районе возле метро Новза. У нас есть квалифицированные преподаватели. Вы можете посмотреть наши онлайн-занятия на YouTube")
    elif message.text == "Курсы":
        await message.answer("В нашем учебном центре доступны арабский, английский, русский языки. Для записи на занятия звоните по телефону +998997630809.")


    elif message.text == "Information":
        await message.answer("Our educational center is located in Chilonzor district near Novza Metro. We have qualified teachers. You can watch our Online classes on YouTub")
    elif message.text == "Courses":
        await message.answer("Arabic, English, Russian languages ​​are available in our training center. To register for classes, contact +998997630809.")
    

    elif message.text == "Telefon raqam":
        await message.answer_contact(phone_number="+998997630809", first_name="Al-Badr", last_name="")
    
    elif message.text == "Joylashuv":
        await message.answer_location(41.288683, 69.220657)
        await message.answer("<b>Bizning manzil</b>: Chilonzor tumani, Novza Metro yaqinida\n<b>Mo'ljal</b>: Trast Bank yonida", parse_mode="HTML")



# @dp.callback_query_handler(lambda b: b.data == "uz")
# async def uzbek(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, "Siz o'zbek tilini tanladingiz", reply_markup=natija2)








if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
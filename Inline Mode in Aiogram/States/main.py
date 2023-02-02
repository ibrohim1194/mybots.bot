import logging 
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
from aiogram.dispatcher import FSMContext
from personaldata import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage



# logging sozlamasi   
logging.basicConfig(level=logging.INFO)



# Botni ulash qismi
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)




@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    ism = message.from_user.first_name
    await message.answer(f"Assalomu alaykum{ism}, Botimizga xush kelibsiz!")



@dp.message_handler(commands=["anketa"])
async def start(message: types.Message):
    await message.answer("To'liq ismingizni kiriting:")
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state=FSMContext):
    full_name = message.text
    #await state.update_data(name=fullname)
    await state.update_data(
        {'fullname': full_name}
    )
    await message.answer("Elektron pochtangizni kiriting:")
    await PersonalData.email.set()








@dp.message_handler(state=PersonalData.email)
async def answer_fullname(message: types.Message, state=FSMContext):
    e_mail = message.text
    #await state.update_data(name=fullname)
    await state.update_data(
        {'email': e_mail}
    )
    await message.answer("Telefon raqamingizni kiriting:")
    await PersonalData.phone.set()








@dp.message_handler(state=PersonalData.phone)
async def answer_fullname(message: types.Message, state=FSMContext):
    phone_number = message.text
    #await state.update_data(name=fullname)
    await state.update_data(
        {'number': phone_number}
    )
    await message.answer("Manzilingizni kiriting:")
    await PersonalData.addres.set()




@dp.message_handler(state=PersonalData.addres)
async def answer_fullname(message: types.Message, state=FSMContext):
    address = message.text
    #await state.update_data(name=fullname)
    await state.update_data(
        {'address': address}
    )
    await message.answer("Tug'ilgan sananingizni kiriting:")
    await PersonalData.dob.set() 





@dp.message_handler(state=PersonalData.dob)
async def answer_fullname(message: types.Message, state=FSMContext):
    date_of_birth = message.text
    #await state.update_data(name=fullname)
    await state.update_data(
        {'date of birth': date_of_birth}
    )

 
    data = await state.get_data()
    name = data.get("fullname")
    email = data.get("email")
    phone_num = data.get("number")
    addres = data.get("address")
    dob_dob = data.get("date of birth")


    msg = "Sizdan quyidagi ma'lumotlar olindi\n\n"
    msg += f"Toliq ismingiz  -  {name}\n\n"
    msg += f"Elektron Pochtangiz  -  {email}\n\n"
    msg += f"Telefon raqam  -  {phone_num}\n\n"
    msg += f"Manzilingiz  -  {addres}\n\n"
    msg += f"Tug'ilgan sanangiz  -  {dob_dob}\n\n"


    await message.answer(msg)

    await state.finish()





if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True) 


   
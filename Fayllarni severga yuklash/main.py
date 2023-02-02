import logging
from aiogram import Bot, Dispatcher,executor,types
from config import API_TOKEN
from aiogram.types import ContentType,Message
from pathlib import  Path

download_path = Path().joinpath("Kategoriya")
download_path.mkdir(parents=True, exist_ok=True)

# Logging sozlamasi
logging.basicConfig(level=logging.INFO)



# Botni ulash qismi
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



# Start buyrug'i
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    ism = message.from_user.first_name
    await message.answer(f"Assalomu alaykum {ism} Botga xush kelibsiz")


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer("Siz matn yubordingiz")




@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download(destination=download_path)
    doc_id = message.document.file_id
    await message.answer(f"Siz Fayl yubordingiz,\n file id={doc_id}")




# @dp.message_handler(commands='fayl')
# async def fayl(message: types.Message):
#     await message.answer_document("BQACAgIAAxkBAANSY9Twz0QryHEpppEpkULr-DjRPkUAAsYeAAKC-qlKH6kz2mROB6ktBA")


@dp.message_handler(content_types=ContentType.VIDEO)
async def vid_handler(message: Message):
    await message.video.download(destination=download_path)
    vid_id = message.video.file_id
    await message.answer(f"Siz Video yubordingiz,\n file id={vid_id}")




@dp.message_handler(content_types=ContentType.PHOTO)
async def vid_handler(message: Message):
    await message.photo[-1].download(destination=download_path)
    rasm_id = message.photo[-1].file_id
    await message.answer(f"Siz rasm yubordingiz,\n file id={rasm_id}")





# Botni ishga tushirish

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)




import logging 
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN



# Logging sozlamasi
logging.basicConfig(level=logging.INFO)




# Botni ulash qismi
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultVideo(
                id = 'video001',
                video_url = "https://www.youtube.com/watch?v=f-iNzatc4h4",
                mime_type = "video/mp4",
                thumb_url="https://www.youtube.com/watch?v=f-iNzatc4h4",
                title = "BMW M5",
                caption="BMW M5 haqida"
            )
        ]
    )









# Botni ishga tushirish qismi
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
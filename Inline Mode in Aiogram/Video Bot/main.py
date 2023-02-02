import logging
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN


# logging sozlamasi
logging.basicConfig(level=logging.INFO)




# Botni ulash qismi
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)





# Inline button funksiyasi
@dp.inline_handler()
async def query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultVideo(
                id = "video001",
                video_url="https://youtube.com/shorts/sdI3GqUtlWw?feature=share",
                mime_type="video/mp4",
                thumb_url="https://youtube.com/shorts/sdI3GqUtlWw?feature=share",
                title="iPhone senda Pro Max",
                caption="iPhone senda Pro Max",
            ),

            types.InlineQueryResultVideo(
                id = "video002",
                video_url="https://youtu.be/Tq4dxVSofXI",
                mime_type="video/mp4",
                thumb_url="https://youtu.be/Tq4dxVSofXI",
                title="Mana Meni Uryapti, Rasmga ol rasmga ol",
                caption="Rasmga ol rasmga ol"
            ),


            types.InlineQueryResultVideo(
                id = "video003",
                video_url="https://youtu.be/B4CBHwVeu64",
                mime_type="video/mp4",
                thumb_url="https://youtu.be/B4CBHwVeu64",
                title="Iye Lutfulla To'rayev",
                caption="Lutfulla Torayev"
            ),



            types.InlineQueryResultVideo(
                id = "video004",
                video_url="https://youtu.be/rtjRylwlVrE",
                mime_type="video/mp4",
                thumb_url="https://youtu.be/rtjRylwlVrE",
                title="Otib tasha hayvonlar",
                caption="Otib tasha"
            ),


            
            types.InlineQueryResultVideo(
                id = "video00",
                video_url="https://youtube.com/shorts/vLAoAeUFqHI?feature=share",
                mime_type="video/mp4",
                thumb_url="https://youtube.com/shorts/vLAoAeUFqHI?feature=share",
                title="O'zbekiston tengdir O'zbekistonga",
                caption="O'zbekistonni alishmasman boshqa jahonga"
            ),


        ]

    )



if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)



from aiogram import *
from pytube import YouTube



bot = Bot("5356705727:AAGrkfqTlyr1dK488YJzgGqrK6iYbi2CEDE")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message:types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Отправь ссылку на видео, которое хочешь скачать")
    



@dp.message_handler()
async def text_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/':
        await bot.send_message(chat_id, f"*Начинаю загрузку видео* : *{yt.title}*\n"
                                f"*C Канала *: [{yt.author}]({yt.channel_url})", parse_mode='Markdown')
        await download_youtube_video(url,message,bot)




async def download_youtube_video(url,message,bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", "rb") as video:
        await bot.send_video(message.chat.id, video, caption="*А вот и ваше видео)*", parse_mode="Markdown")
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}") 






if __name__ == '__main__':
    executor.start_polling(dp)




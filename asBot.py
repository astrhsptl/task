import os
import asyncio
from PIL import Image
from telebot.async_telebot import AsyncTeleBot

from compressor import archive, dearchive 
from preprocessor import getPreprocessedImage

token = '5939461261:AAG13zKhpMhF3XQ-jGhZKK6k2Se44182Ovw'
bot = AsyncTeleBot(token)


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Привет) Я - бот комадны FV 3R&1B).
Вышли мне картинку с текстом).
""")

@bot.message_handler(content_types=['photo'])
async def handle_photo(message):
    try:
        file_info = (await bot.get_file(message.photo[-1].file_id)).file_path
        downloaded_file = (await bot.download_file(file_info))
    
        imageName = f'tempFiles/{message.photo[-1].file_id}.jpg'
        archiveName = f'tempFiles/{message.photo[-1].file_id}.zip'
    
        f = open(imageName, 'wb').write(downloaded_file)
        Image.fromarray(getPreprocessedImage(imageName, False)).save(imageName)
    
        archive(archiveName, {imageName})
        dearchive(archiveName, 'tempFiles/')

        img = open(imageName, 'rb')
        await bot.send_photo(message.from_user.id, img)
        os.remove(imageName)
        os.remove(archiveName)
    except:
        await bot.send_message(message.from_user.id, '''\
Что-то с изображением не то (''')
        await os.remove(imageName)

asyncio.run(bot.polling(non_stop=True)) 
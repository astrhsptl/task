import os
import asyncio
from PIL import Image
from telebot.async_telebot import AsyncTeleBot

from preprocessor import getPreprocessedImage

token = ''

bot = AsyncTeleBot(token)


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Привет) Я - бот комадны FV 3R&1B).
Вышли мне картинку с текстом).
""")

@bot.message_handler(content_types=['photo'])
async def handle_photo(message):
    file_info = (await bot.get_file(message.photo[-1].file_id)).file_path
    downloaded_file = (await bot.download_file(file_info))
    fileName = f'tempFiles/{message.photo[-1].file_id}.jpg'
    f = open(fileName, 'wb').write(downloaded_file)
    Image.fromarray(getPreprocessedImage(fileName, False)).save(fileName)
    img = open(fileName, 'rb')
    await bot.send_photo(message.from_user.id, img)
    await os.remove(fileName)

asyncio.run(bot.polling(non_stop=True)) 
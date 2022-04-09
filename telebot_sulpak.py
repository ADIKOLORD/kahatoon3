from bs4 import BeautifulSoup
import requests

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '5285474379:AAGPQd_o2lg3SAMXL7SkOhcNfzdSufH8jIQ'

URL = requests.get('https://www.sulpak.kg/f/noutbuki/bishkek/846_47', verify=False).text
soup = BeautifulSoup(URL, features="html.parser")
data = soup.find('ul', class_='goods-container').find_all('li', class_='tile-container')

name, link, photo, price, buy = [], [], [], [], []
for i in data:
    vname = i.find('h3', class_='title').text
    vlink = 'https://www.sulpak.kg' + i.find('a').get('href')
    vphoto = i.find('img', class_='image-size-cls')['src']
    vprice = i.find('div', class_='price').text
    vbuy = i.find('span', class_='availability').text
    name.append(vname)
    link.append(vlink)
    photo.append(vphoto)
    price.append(vprice)
    buy.append(vbuy)

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_bot(msg: types.Message):
    btn = types.KeyboardButton('ALL COMPUTERS')
    btn2 = types.KeyboardButton('ONLY NAME')
    btn3 = types.KeyboardButton('ONLY PRICE')
    btn4 = types.KeyboardButton('ONLY PHOTO')
    btn_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_markup.add(btn)
    btn_markup.row(btn2, btn3, btn4)
    await msg.reply(f'Hello, {msg.from_user.username}\nChoose the command!', reply_markup=btn_markup)


@dp.message_handler()
async def show_computer(msg: types.Message):
    word = msg.text
    if word == 'ALL COMPUTERS':
        for i in range(len(name)):
            await bot.send_photo(msg.from_user.id, photo=photo[i])
            await msg.answer(f"Name: {name[i]}\nLink: {link[i]}\nЦена: {price[i]}\nВ наличии: {buy[i]}")






executor.start_polling(dp)
import telebot
import requests
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
token = 'СЮДА ВСТАВЬ СВОЙ ТОКЕН'
bot = telebot.TeleBot(token)
murcup = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton('курс доллара',callback_data='dollar')
btn2 = InlineKeyboardButton('погода в Москве',callback_data='wind')
murcup.add(btn1,btn2)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'привет я бот для курса валют, выберите:',reply_markup=murcup)

@bot.callback_query_handler(func=lambda x:True)
def hand(x):
    if x.data == 'dollar':
        repose = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        r = repose.json()
        usd = r['rates']['RUB']
        bot.send_message(x.message.chat.id,f'{usd}')
    elif x.data == 'wind':
        url = 'https://wttr.in/Moscow?format=j1'
        response = requests.get(url)
        data = response.json()
        temp = data['current_condition'][0]['temp_C']
        desc = data['current_condition'][0]['weatherDesc'][0]['value']
        bot.send_message(x.message.chat.id, f'В Москве сейчас {desc}, {temp}°C')
#test

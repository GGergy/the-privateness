import telebot
from telebot import types

bot = telebot.TeleBot('6154244462:AAEnaVAg2JA9wvv7c79BlfhdZupUrI1x0ak')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('click', web_app=telebot.types.WebAppInfo(url='https://itproger.com'))
    markup.row(btn)
    bot.send_message(message.chat.id, text='a', reply_markup=markup)


bot.infinity_polling()

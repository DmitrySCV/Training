import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    sti = open('C:/Users/acer/telegram/11.gif', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'Привет! Я мини-работ! \n Мой хозяин создал меня для демонстрации того, что он умеет "играть на пианино.'
                                      '\n Как любой робот, я готов помогать Человеку! Напиши мне"')
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет' or "Hello" or "Hi":
        sti = open('C:/Users/acer/telegram/22.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, user')
# RUN
bot.polling(none_stop=True)



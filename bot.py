# -*- coding: utf-8 -*-

import config

import telebot

#from telebot import apihelper

bot = telebot.TeleBot(config.token, threaded=False)

#apihelper.proxy = {
#    'http': 'socks5://138.197.58.55:1080',
#    'https': 'socks5://138.197.58.55:1080'
#    }

#@bot.message_handler(commands=['start'])
    
#def start_handler(message):

#    answer = 'Здравствуйте, этот бот представляет Церковь Христианская Миссия'
    
#    bot.send_message(message.chat.id, answer)


#@bot.message_handler(comands=['help'])

#def help_handler(message):
    
#    answer = '''На данный момент поддерживаются 4 команды,
#             /contacts Предоставляет информацию о наших контактах
#             /links Предоставляет ссылки на наши чаты и соцсети
#             /hotline Горячая линия телеграме с нашими служителями
#             /informations Полезная информация'''
    
#    bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=["text"])

def repeat_all_messages(message):
    
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__': 
    
    while True:
        
        try:
            
            bot.polling(none_stop=True) 
            
        except Exception as e: 
            
            print(e)
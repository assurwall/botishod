# -*- coding: utf-8 -*-

import config

import telebot

#from telebot import apihelper

bot = telebot.TeleBot(config.token, threaded=False)

#apihelper.proxy = {
#    'http': 'socks5://138.197.58.55:1080',
#    'https': 'socks5://138.197.58.55:1080'
#    }

@bot.message_handler(content_types="text")
    
def start_handler(message):

    answer = 'Здравствуйте, этот бот представляет Церковь Христианская Миссия'
    
    bot.send_message(message.chat.id, answer)


@bot.message_handler(comands=['help'])

def help_handler(message):
    
    answer = '''На данный момент поддерживаются 4 команды,
             /contacts Предоставляет информацию о наших контактах
             /links Полезные ссылки
             /hotline Горячая линия телеграме с нашими служителями
             /informations О нас
             /legal Юридический уголок'''
    
    bot.send_message(message.chat.id, answer)


if __name__ == '__main__': 
    
    while True:
        
        try:
            
            bot.polling(none_stop=True) 
            
        except Exception as e: 
            
            print(e)
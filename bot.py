# -*- coding: utf-8 -*-

import config

import telebot

bot = telebot.TeleBot(config.token, threaded=False)

@bot.message_handler(content_types="text")

def test_handler(message):

    print(message.text())

    if(message.text()=='/start'):
    
        answer = 'Здравствуйте, этот бот представляет Церковь Христианская Миссия'
        
    if(message.text()=='/help'):
    
        answer = '''На данный момент поддерживаются 5 команд,
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
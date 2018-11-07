# -*- coding: utf-8 -*-

import config

import telebot

from telebot import types

bot = telebot.TeleBot(config.token, threaded=False)


@bot.message_handler(content_types="text")

def text_handler(message):

    if(message.text=='/start'):
    
        answer = 'Здравствуйте, этот бот представляет Здоровое Черноземье'
        
        bot.send_message(message.chat.id, answer)
    

    elif(message.text=='/help'):
    
        hotline_button=types.KeyboardButton(text='Горячая линия',url='')
        
        informations_button=types.KeyboardButton(text='О нас',url='')
        
        contacts_button=types.KeyboardButton(text='Контакты',url='')
        
        links_button=types.KeyboardButton(text='Полезные ссылки',url='')
        
        legal_button=types.KeyboardButton(text='Юридический уголок',url='')
        
        
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        
        markup.add(hotline_button)
        
        markup.add(informations_button)
        
        markup.add(contacts_button)
        
        markup.add(links_button)
        
        markup.add(legal_button)
        
        
        bot.send_message(message.chat.id, 'Выберите интересующий пункт из меню.', reply_markup = markup)
        
        
    else:
    
        bot.send_message(message.chat.id, "Я вас не понимаю.")
        

if __name__ == '__main__': 
    
    while True:
        
        try:
            
            bot.polling(none_stop=True) 
            
        except Exception as e: 
            
            print(e)
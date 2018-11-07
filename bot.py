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
    
        hotline_button=types.KeyboardButton(text='Горячая линия')
        
        informations_button=types.KeyboardButton(text='О нас')
        
        contacts_button=types.KeyboardButton(text='Контакты')
        
        links_button=types.KeyboardButton(text='Полезные ссылки')
        
        legal_button=types.KeyboardButton(text='Юридический уголок')
        
        
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        
        keyboard.add(hotline_button)
        
        keyboard.add(informations_button)
        
        keyboard.add(contacts_button)
        
        keyboard.add(links_button)
        
        keyboard.add(legal_button)
        
        
        bot.send_message(message.chat.id, 'Выберите интересующий пункт из меню.', reply_markup = keyboard)
        
        
    else:
    
        bot.send_message(message.chat.id, "Я вас не понимаю.")
        

if __name__ == '__main__': 
    
    while True:
        
        try:
            
            bot.polling(none_stop=True) 
            
        except Exception as e: 
            
            print(e)
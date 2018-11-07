# -*- coding: utf-8 -*-

import config

import telebot


bot = telebot.TeleBot(config.token, threaded=False)


@bot.message_handler(content_types="text")

def text_handler(message):

    if(message.text=='/start'):
    
        answer = 'Здравствуйте, этот бот представляет Здоровое Черноземье'
        
        bot.send_message(message.chat.id, answer)
    

    elif(message.text=='/help'):
    
        hotline_button=telebot.types.InlineKeyboardButton(text='Горячая линия',url='')
        
        informations_button=telebot.types.InlineKeyboardButton(text='О нас',url='')
        
        contacts_button=telebot.types.InlineKeyboardButton(text='Контакты',url='')
        
        links_button=telebot.types.InlineKeyboardButton(text='Полезные ссылки',url='')
        
        legal_button=telebot.types.InlineKeyboardButton(text='Юридический уголок',url='')
        
        
        markup=telebot.types.InlineKeyboardMarkup()
        
        
        markup.add(hotline_button)
        
        markup.add(informations_button)
        
        markup.add(contacts_button)
        
        markup.add(links_button)
        
        markup.add(legal_button)
        
        
        bot.send_message(message.chat.id, "Выберите интересующий пункт из меню.", reply_markup = markup)


if __name__ == '__main__': 
    
    while True:
        
        try:
            
            bot.polling(none_stop=True) 
            
        except Exception as e: 
            
            print(e)
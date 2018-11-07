# -*- coding: utf-8 -*-

import config

import telebot

from telebot import types

bot = telebot.TeleBot(config.token, threaded=False)

def main_menu():

#    hotline_button=types.InlineKeyboardButton(text='Горячая линия', callback_data='hotline_query')
        
#    informations_button=types.InlineKeyboardButton(text='О нас', callback_data='informations_query')
        
#    contacts_button=types.InlineKeyboardButton(text='Контакты', callback_data='contacts_query')
        
#    links_button=types.InlineKeyboardButton(text='Полезные ссылки', callback_data='links_query')
        
#    legal_button=types.InlineKeyboardButton(text='Юридический уголок', callback_data='legal_query')
        
    buttons = [
                types.InlineKeyboardButton(text='Горячая линия', callback_data='hotline_query'),
                types.InlineKeyboardButton(text='О нас', callback_data='informations_query'),
                types.InlineKeyboardButton(text='Контакты', callback_data='contacts_query'),
                types.InlineKeyboardButton(text='Полезные ссылки', callback_data='links_query'),            
                types.InlineKeyboardButton(text='Юридический уголок', callback_data='legal_query')
                ]
    
    keyboard=types.InlineKeyboardMarkup()
        
        
#    keyboard.add(hotline_button)
        
#    keyboard.add(informations_button)
        
#    keyboard.add(contacts_button)
        
#    keyboard.add(links_button)
        
#    keyboard.add(legal_button)

    for button in buttons:
    
        keyboard.add(button)
    
    return keyboard


@bot.message_handler(content_types="text")

def text_handler(message):

    if(message.text=='/start'):
    
        answer = 'Здравствуйте, этот бот представляет Здоровое Черноземье'
        
        bot.send_message(message.chat.id, answer)
    
    elif(message.text=='/help'):
        
        bot.send_message(message.chat.id, 'Выберите интересующий пункт из меню.', reply_markup = main_menu())
        
#    else:
    
#        bot.send_message(message.chat.id, 'Я вас не понимаю.')


@bot.callback_query_handler(func=lambda inline_query: True)

def inline_handler(inline_query):

    if(inline_query.data=='hotline_query'):
        
        keyboard=types.InlineKeyboardMarkup()
        
        help_button=types.InlineKeyboardButton(text='Помощь', url='https://t.me/Pomoth')
        
        chat_button=types.InlineKeyboardButton(text='Чат, если бан', url='https://t.me/joinchat/HUGe2kdgu8_3lkWy2qvrvA')
        
        back_button=types.InlineKeyboardButton(text='Назад', callback_data='main_menu_query')
        
        keyboard.add(help_button)
        
        keyboard.add(chat_button)
        
        keyboard.add(back_button)
    
        bot.edit_message_text(
            
                chat_id=inline_query.message.chat.id,
                
                message_id=inline_query.message.message_id,
    
                text='Вы можете позвонить нам по бесплатному номеру '
                '8-800-333-09-81, '
                'Пишите нам: @Yarik78, @Zaosi',
                
                reply_markup=keyboard,
                                    
                parse_mode='Markdown')
    
    if(inline_query.data=='main_menu_query'):

        bot.edit_message_text(
            
                chat_id=inline_query.message.chat.id,
                
                message_id=inline_query.message.message_id,
    
                text='Выберите интересующий пункт из меню.',
                
                reply_markup=main_menu(),
                                    
                parse_mode='Markdown')
        
        
if __name__ == '__main__': 
    
    while True:
        
        try:
            
            bot.polling(none_stop=True) 
            
        except Exception as e: 
            
            print(e)
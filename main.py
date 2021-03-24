#!/usr/bin/python3.6
import telebot

bot = telebot.TeleBot('1572674420:AAHz_p68py7VbSClOjK_RY0_m_P_bmWgsgc')

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = "<br>Hello {message.from_user.first_name}{message.from_user.last_name}</br>!"
    bot.send_message(message.chat.id, send_mess, parse_mode = 'html')

bot.polling(none_stop=True)

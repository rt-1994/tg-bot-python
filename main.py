import telebot

bot = telebot.TeleBot("1572674420:AAHz_p68py7VbSClOjK_RY0_m_P_bmWgsgc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
import datetime
import telebot

def send_message(text, bot):
    chat_id = 5046185897
    bot.send_message(chat_id, text)

if __name__ == '__main__':
    BOT_TOKEN = '6636169941:AAFysc5k-IA1QCC-1tfKXeTC_qeIdcG15ZI'

    bot = telebot.TeleBot(BOT_TOKEN)    
    send_message("okay, BOZO!", bot)

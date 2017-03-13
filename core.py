# -*- coding: utf-8 -*-
import hbb_constants
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import congrats_db
from emoji import emojize
import os
import time
import sys
import videos
import csv
from datetime import datetime



updater = Updater(token=hbb_constants.API_key)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(bot,update):
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('photo_2017-03-12_18-32-19.jpg','rb'))
    bot.sendMessage(chat_id=update.message.chat_id, text = hbb_constants.start_text)

keyboard = congrats_db.keyboard

def main_menu(bot, update):
    text = emojize("Это все твои подарки, открывай! :gift:", use_aliases=True)
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.sendMessage(chat_id=update.message.chat_id, reply_markup=reply_markup, text=text)

def logging(item):
    with open('logs.csv', 'a+') as csvfile:
        logswriter = csv.writer(csvfile, delimiter='\t')
        log = [str(datetime.now()), item]
        logswriter.writerow(log)




def button(bot, update):
    query = update.callback_query
    option = query.data
    keyboard_back = [[InlineKeyboardButton(" <<< ", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard_back)

    if option == 'back':
        text = emojize('Это все твои подарки, открывай!   :gift: \n', use_aliases=True)
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.sendMessage(chat_id=query.message.chat.id, text=text, reply_markup=reply_markup,message_id=query.message.message_id)

    if option == 'with body and mind from CyberfunCommunity':
        bot.sendPhoto(chat_id=query.message.chat.id, photo=open(congrats_db.congratulations_db[option],'rb'))
        bot.sendMessage(chat_id=query.message.chat.id, text='Вернуться к списку', reply_markup=reply_markup,
                        message_id=query.message.message_id, parse_mode='HTML')


    else:

        bot.sendVideo(chat_id=query.message.chat.id,video=open(congrats_db.congratulations_db[option], 'rb'))
        bot.sendMessage(chat_id=query.message.chat.id, text='Вернуться к списку', reply_markup=reply_markup,
                        message_id=query.message.message_id, parse_mode='HTML')

    logging(option)

start_handler = CommandHandler('start', start)
main_menu_handler = CommandHandler('happy_birthday_me', main_menu)
dispatcher.add_handler(CallbackQueryHandler(button))

dispatcher.add_handler(start_handler)
dispatcher.add_handler(main_menu_handler)

def restart(bot, update):
    bot.sendMessage(update.message.chat_id, "Bot is restarting...Press /start")
    time.sleep(0.2)
    os.execl(sys.executable, sys.executable, *sys.argv)

dispatcher.add_handler(CommandHandler('r', restart))


if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
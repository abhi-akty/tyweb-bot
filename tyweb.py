from telegram.ext import Updater,CommandHandler
from telegram import ChatAction
from datetime import datetime, timedelta
from pytz import timezone
from time import sleep
import logging,requests,pytz,re,ast

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

updater=Updater(token='348150272:AAGxwP_4HYPatjn60mc6HRcxlS2K9hi_80s')
dispatcher=updater.dispatcher


utc = pytz.utc


print("I'm On..!!")

def start(bot, update, args):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id,text='''
Hello, I am glad u stopped BY! Welcome to the world of tyweb''')

def website(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id,text='Oops still working on it')



def invitelink(bot,update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id, text='Join here : https://telegram.me/joinchat/Fx0cXQ1w24n8_l5um3Q2Rw')



def github(bot,update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id, text='Github repo link - https://github.com/abhi-akty/tyweb-bot')



def help(bot, update):
	bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
	sleep(0.2)
	bot.sendMessage(chat_id=update.message.chat_id, text='''
Use one of the following commands
/start - to get a fresh start
/invitelink - to get an invite link
/website - to get our official website
/call - to call members for a match
/github - for github repo link to contribute

Any kind of suggestions and improvements will be greatly honored.


''')
def call(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="This command will call all users of this group individually for a match(still working on it)")

dispatcher.add_handler(CommandHandler('start', start, pass_args=True))

dispatcher.add_handler(CommandHandler('website', website))

dispatcher.add_handler(CommandHandler('invitelink', invitelink))

dispatcher.add_handler(CommandHandler('help', help))

dispatcher.add_handler(CommandHandler('call', call))

dispatcher.add_handler(CommandHandler('github', github))

updater.start_polling()

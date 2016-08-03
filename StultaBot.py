#!/usr/bin/env python
from telegram.ext import Updater, CommandHandler, MessageHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def add_commands(dp):
	import modules.Base as Base
	dp.add_handler(CommandHandler("start", Base.start))
	dp.add_handler(CommandHandler("help", Base.help))
	dp.add_handler(CommandHandler("getuser", Base.get_user))
	dp.add_handler(CommandHandler("getchat", Base.get_chat))
	import modules.Key as Key
	Key.main(dp)
	import modules.Testing as Testing
	Testing.main(dp)

def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))
def main():
	f = open('token.txt')
	token = f.read()
	updater = Updater(token)
	dp = updater.dispatcher
	add_commands(dp)
	dp.add_error_handler(error)
	updater.start_polling()
	updater.idle()

main()

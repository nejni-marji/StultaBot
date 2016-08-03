#!/usr/bin/env python
from telegram.ext import CommandHandler, MessageHandler

def oh_god(bot, update):
	print('oh god')
	return None
	if update.message.text.lower().contains('oh god'):
		bot.sendMessage(
			update.message.chat_id,
			'_Harder, harder!_',
			parse_mode = telegram.ParseMode.MARKDOWN
		)

def main(dp):
	dp.add_handler

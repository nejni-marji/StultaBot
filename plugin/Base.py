#!/usr/bin/env python

def start(bot, update):
	bot.sendMessage(update.message.chat_id, text = 'Started!')

def help(bot, update):
	bot.sendMessage(update.message.chat_id, text = 'TBA')

def get_user(bot, update):
	if update.message.reply_to_message != None:
		bot.sendMessage(
			update.message.chat_id,
			update.message.reply_to_message.from_user['id'],
		)

def get_chat(bot, update):
	bot.sendMessage(
		update.message.chat_id,
		update.message.chat_id,
	)

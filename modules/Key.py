#!/usr/bin/env python
from telegram.ext import CommandHandler, MessageHandler
from telegram import ParseMode
import os

import modules.DataBase as DataBase
import modules.SuperUser as SuperUser

def extract_keys(message):
	text = message.text
	key_list = []
	for e in message.entities:
		if e.type == 'hashtag':
			key_list.append(text[e.offset+1:e.offset+e.length]) # string of MessageEntity
	return key_list

def arg_key(args):
	return args.pop(0)[1:]

def add_local_key(bot, update, args):
	#if ADMIN: #todo: fix this
		key = arg_key(args)
		if key == extract_keys(update.message)[0]:
			DataBase.add_key(
				update.message.chat_id,
				key,
				' '.join(args)
			)
			bot.sendMessage(
				update.message.chat_id,
				'Added "{}".'.format(key)
			)

def add_global_key(bot, update, args):
	if SuperUser.sudoer(update.message.from_user['id']):
		key = arg_key(args)
		if key == extract_keys(update.message)[0]:
			DataBase.add_key(
				'global',
				key,
				' '.join(args)
			)
			bot.sendMessage(
				update.message.chat_id,
				'Added global "{}".'.format(key)
			)

def del_local_key(bot, update, args):
	#if ADMIN: #todo: fix this
		DataBase.del_key(
			update.message.chat_id,
			args.pop(0)[1:]
		)

def del_global_key(bot, update, args):
	if SuperUser.sudoer(update.message.from_user['id']):
		DataBase.del_key(
			'global',
			args.pop(0)[1:]
		)

def get_local_keys(bot, update):
	bot.sendMessage(
		update.message.from_user['id'],
		DataBase.get_keys(update.message.chat_id),
		disable_web_page_preview = True,
		parse_mode = ParseMode.MARKDOWN
	)

def get_global_keys(bot, update):
	bot.sendMessage(
		update.message.from_user['id'],
		DataBase.get_keys('global'),
		disable_web_page_preview = True,
		parse_mode = ParseMode.MARKDOWN
	)

def get_value(bot, update):
	for key in extract_keys(update.message):
		try:
			bot.sendMessage(
				update.message.chat_id,
				DataBase.get_value(update.message.chat_id, key),
				parse_mode = ParseMode.MARKDOWN
			)
		except TypeError:
			pass


def main(dp):
	dp.add_handler(CommandHandler("add", add_local_key, pass_args = True))
	dp.add_handler(CommandHandler("gadd", add_global_key, pass_args = True))
	dp.add_handler(CommandHandler("del", del_local_key, pass_args = True))
	dp.add_handler(CommandHandler("gdel", del_global_key, pass_args = True))
	dp.add_handler(CommandHandler("get", get_local_keys))
	dp.add_handler(CommandHandler("gget", get_global_keys))
	dp.add_handler(MessageHandler([], get_value))

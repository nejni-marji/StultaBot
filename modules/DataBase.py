#!/usr/bin/env python
import json, os

key_file = 'key_file.json'
# load key_file
keychain = json.load(open(key_file, 'r'))
keychain_lower = {}
for chat_id in keychain:
	if chat_id == 'global': continue
	keychain[int(chat_id)] = keychain.pop(chat_id)

def add_key(chat_id, key, value): #neo
	if chat_id not in keychain:
		keychain[chat_id] = {} # fuckin' put it in m8
	keychain[chat_id][key.lower()] = {'title': key, 'value': value}
	# dump key_file
	json.dump(keychain, open(key_file, 'w'))

def del_key(chat_id, key):
	try:
		keychain[chat_id].pop(key.lower())
	except KeyError:
		pass
	# dump key_file
	json.dump(keychain, open(key_file, 'w'))

def get_keys(chat_id):
	keys = []
	for key in keychain[chat_id]:
		key = keychain[chat_id][key]
		keys.append('*#{}:* {}'.format(
			key['title'],
			key['value']
		))
	return '\n'.join(keys)

def get_value(chat_id, key): #neo
	key = key.lower()
	# we want to check global first, so see if key is in it
	if key in keychain.get('global'):
		key = keychain['global'].get(key)
	elif key in keychain.get(chat_id):
		key = keychain[chat_id].get(key)
	return key['value']

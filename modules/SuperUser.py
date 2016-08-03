#!/usr/bin/env python
sudoers = (
	96761380, # @nejni_marji
	26927785, # @Robin
#	101566181, # @Pritchenko
#	237799109, # @Diulo/@Bestulo
#	261243065, # Louis
#	2889459, # @Furetino (Ari)
)
def sudoer(user_id):
	return user_id in sudoers

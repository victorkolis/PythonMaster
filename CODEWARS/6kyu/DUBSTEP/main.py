import re

# 'WUBAWUB' -> 'A', remove all the WUBs, WUBWUB = ' ', ' A ' is not allowed

def song_decoder(text):
	text = text.replace('WUBWUBWUB', ' ').replace('WUBWUB', ' ').replace('WUB', ' ')
	
	return text

print(song_decoder('AWUBWUBWUBBWUBWUBWUBC'))

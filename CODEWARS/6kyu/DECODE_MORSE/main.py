#!/usr/bin/env python3

# .- -> A

def decodeMorse(text):
	morse = {
		'...---...': "SOS",
		''   : " ",
		'.-'	: "A",
		'-...'	: "B",
		'-.-.'	: "C",
		'-..'	: "D",
		'.'		: "E",
		'..-.'	: "F",
		'--.'	: "G",
		'....'	: "H",
		'..'	: "I",
		'.---'	: "J",
		'-.-'	: "K",
		'.-..'	: "L",
		'--'	: "M",
		'-.'	: "N",
		'---'	: "O",
		'.--.'	: "P",
		'--.-'	: "Q",
		'.-.'	: "R",
		'...'	: "S",
		'-'		: "T",
		'..-'	: "U",
		'...-'	: "V",
		'.--'	: "W",
		'-..-'	: "X",
		'-.--'	: "Y",
		'--..'	: "Z",
		'.----'	: "1",
		'..---'	: "2",
		'...--'	: "3",
		'....-'	: "4",
		'.....'	: "5",
		'-....'	: "6",
		'--...'	: "7",
		'---..'	: "8",
		'----.'	: "9",
		'-----'	: "0",
		'.-.-.-': ".",
		'--..--': ",",
		'-.-.--': "!",
		'..--..': "?",
		
	}
	
	message = ''
	try:
		for element in text.split(' '):
			message += morse[element]
		
		return message.replace('  ', ' ').strip()
	except KeyError:
		pass
		
		
print(decodeMorse('.... . -.--   .--- ..- -.. .'))

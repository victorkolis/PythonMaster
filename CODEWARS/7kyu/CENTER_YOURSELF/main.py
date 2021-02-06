#!/usr/bin/env python3

def center(s, width, fill=' '):
	return f'{fill}{s.center(width, fill)[0:width - 1]}'


print(center('ab', 5, '_'))

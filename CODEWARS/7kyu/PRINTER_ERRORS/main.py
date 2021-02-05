#!/usr/bin/env python3

# The only allowed letters are a-m the rest is considered error
# Print the error rate from this printer

import re


def printer_error(s):
	return f"{len(re.findall(r'[^a-m]', s))}/{len(s)}"
	

print(printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))

#!/usr/bin/env python3

import re

text = '''
I am victor
i aM Victor
i Am VICtor
i AM vICTOR
'''

print(re.findall(r'[Vv]ictor', text))
print(re.findall(r'[Vv][Ii][Cc][Tt][Oo][Rr]', text))

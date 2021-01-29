#!/usr/bin/env python3

import re

text = '''
I am victor
i aM Victor
i Am VICtor
i AM vICTOR
i am aictor
He is wictor
they are mictor
It's viktor
'''


print(re.findall(r'[Vv]ictor', text))
print(re.findall(r'[Vv][Ii][Cc][Tt][Oo][Rr]', text))

# Range
print(re.findall(r'[a-v]ictor', text))

print(re.findall(r'[a-zA-Z0-9]ictor', text))


# Flags, re.I = re.IGNORECASE

print(re.findall(r'victor', text, flags=re.IGNORECASE))

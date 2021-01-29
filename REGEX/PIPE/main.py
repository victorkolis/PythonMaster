#!/usr/bin/env python3

# . ^ $ * + ? { } [ ] \ | ( )

import re
import sys
sys.path.append('../')

from text_file import text



# PIPE, |, or

print(re.findall(r'gorgeous|of', text))
print(re.findall(r'g...eous|.f', text))

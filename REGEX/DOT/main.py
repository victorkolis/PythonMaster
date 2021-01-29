#!/usr/bin/env python3

import re
import sys
sys.path.append('../')

from text_file import text

# DOT

print(re.findall(r'Gorgeous|gorgeous', text))

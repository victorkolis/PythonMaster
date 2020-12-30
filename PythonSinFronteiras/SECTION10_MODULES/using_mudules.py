# This file is importing a created module called 'modules' which is contained in this directory

import modules
import modules as md
from modules import *

for person in modules.people:
    print(modules.greet(person))  # import modules

print(md.people)  # import modules as md
print(greet('Victor'))  # from modules import *


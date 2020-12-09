# This software objective is to find/figure out how many occurrencies of o given letter-character happens in a given text

import pprint
import string 

# text = '''
# The wolf justifying his right to eat the lamb.
# 
# A WOLF, meeting with a lamb astray from the fold, resolved not to lay violent hands on him, but to find some plea, which should justify to the lamb himself, his right to eat him.
# 
# He then addressed him: "Sirrah, last year you grossly insulted me."
# "Indeed," bleated the lamb in a mournful tone of voice: "I was not then born."
# 
# Then said the wolf: "You feed in my pasture."
# "No, good sir," replied the lamb: "I have not yet tasted grass."
# 
# Again said the wolf: "You drink of my well."
# "No," exclaimed the lamb: "I never yet drank water, for as yet my mother's milk is both food and drink to me."
# 
# Upon which the wolf seized him and ate him up, saying: "Well! I won't remain supper-less, even though you refute every one of my imputations."
# 
# '''

text = input('Type in a text: ').upper()

text = list(text)

occurrencies = {}
for letter in text:
    
    if letter not in string.ascii_letters:
        continue
    
    elif letter not in occurrencies.keys():
        occurrencies[letter] = text.count(letter)

pprint.pprint(occurrencies)

#!/usr/bin/env python3

# Delete anything that has already shown up in the "geese" array

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
	new_birds = []
	for element in birds:
		if element in geese:
			pass
		else:
			new_birds += [element]
			
	return new_birds

print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))
print(goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]))
print(goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]))  # should return -> []

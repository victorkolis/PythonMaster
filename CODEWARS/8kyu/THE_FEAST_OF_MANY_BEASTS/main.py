#!/usr/bin/env python3

# Check whether the beast and the dish start and end with the same letters

def feast(beast: str, dish: str) -> bool:
	return True if beast[0] == dish[0] and beast[len(beast) - 1] == dish[len(dish) - 1] else False


print(feast("great blue heron", "garlic naan"))  # True

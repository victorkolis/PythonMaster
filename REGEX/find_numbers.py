import re

message = 'This is Code Future Invent if you want to contact us please dial 313-555-0107 or 313-555-9872'

phone_finder_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Search
match_object = phone_finder_regex.search(message)
number = match_object.group()
print(number)


# Findall
numbers = phone_finder_regex.findall(message)
print(numbers)


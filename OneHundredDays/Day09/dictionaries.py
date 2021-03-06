# dictionaries.py

# key | value

programming_dictionary = {
    "Bug": "An unexpected defect, fault, flaw, or imperfection.",
    "Function": "A piece of code that you can easily call.",
    }

# Retrieving info from a dictionary by key
print(programming_dictionary["Bug"])

# Dynamically adding a piece of data to a dictionary key+value
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Creating an empty dictionary
empty_dictionary = {}

# Retrieving info from a dictionary by index
print(programming_dictionary)

# Loop through the dictionary (retrieve all the data)
for key in programming_dictionary:
    print(f'{key}: {programming_dictionary[key]}')

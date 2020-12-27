import datetime

current_time = datetime.datetime.now()
victor_kolis = {'name': 'Victor Kolis Ford', 'age': str(current_time.year - 1994), 'ID': '314159'}
print(victor_kolis)

# Getting value
value = victor_kolis.get('age')
# or, value = victor_kolis['age']
# All values
values = list(victor_kolis.values())

print(value)
print(values)

# Getting key
key = victor_kolis.keys()
print(list(key)[1])


# Getting the key and value
for k, v in victor_kolis.items():
    print(f'{k}: {v}')


# Changing the value of a key
victor_kolis['name'] = 'Vinicius'

# Dynamically creating new keys
victor_kolis['address'] = '404, Not Found Street'
print(victor_kolis)

# Checking whether a key exists
print(victor_kolis.get('profession', 'key not found'))

# Deleting specific key
del victor_kolis['ID']
print(victor_kolis)

# Deleting the entire dictionary
# del victor_kolis (This deletes the variable reference)
victor_kolis.clear()  # This wipes the dictionary
print(victor_kolis)


# Getting multiple values inputted and storing them
client = []
f_name, m_name, l_name = input('Enter your First Middle Last name: ').title().split()
client.append({'f_name': f_name, 'm_name': m_name, 'l_name': l_name})

print(client)

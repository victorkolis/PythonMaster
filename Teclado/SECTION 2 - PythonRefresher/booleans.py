print(5 == 5.0)
print(5 > 5)
print(5 != 5)
print(5 is not 5)

# Comparisons: ==, !=, >, <, >=, <=,

# Comparing lists
friends = ['Victor', 'Vinicius']
abroad = ['Victor', 'Vinicius']

# In this case Python is comparing the actual value
print(friends == abroad)

# In this case Python is comparing the memory location rather than the actual value
print(friends is abroad)

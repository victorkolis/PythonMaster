# add_only_the_even.py

even_added = 0


for number in range(1, 101):
    if(number % 2 == 0):
        even_added += number
print(even_added)


# or
even_added = 0
for number in range(2, 101, 2):
    even_added += number
print(even_added)
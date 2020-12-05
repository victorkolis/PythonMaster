# while_loop.py

spam = 0
while spam < 5:
    print("spam")
    spam += 1

# while runs until a certain need is fulfilled until then the code can and-
# will execute

name = ''
while name != "your name":
    name = input("Type your name: ")
print("Thank you!")

# using break
name = ''
while True:
    name = input("Type your name: ")
    if name == "your name":
        break
print("Thank you!")

# This software objective is to invert two variable values into each other without losing content

a = input("a: ")
b = input("b: ")

a, b = b, a

# another possible way
# c = a
# a = b
# b = c 

print("a: " + a)
print("b: " + b)

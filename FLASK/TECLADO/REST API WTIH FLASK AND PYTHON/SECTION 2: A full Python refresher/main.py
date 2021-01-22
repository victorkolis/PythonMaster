# Lambda functions do essentially function as value returners
# EXAMPLE 1
add = (lambda x, y: x + y)(5, 7)
print(add)


# EXAMPLE 2
def double(x):
    return x * 2


# List comprehensions over maps (In computing speed matters)
sequence = [2, 3, 5, 7]
doubled1 = [double(x) for x in sequence]  # or map
doubled2 = list(map(double, sequence))

# Using lambda
doubled3 = [(lambda x: x * 2)(x) for x in sequence]

print(doubled1, doubled2)

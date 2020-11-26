# range_object.py

print(range(10))

# One argument
for i in range(10):
    print(f"for i in range(10): {i}")

print("\n")
# Two arguments
for i in range(2, 10):
    print(f"for i in range(2, 10): {i}")

print("\n")
# Three arguments ascending
for i in range(2, 10, 2):
    print(f"for i in range(2, 10, 2): {i}")

print("\n")
# Three arguments descending
for i in range(2, -10, -1):
    print(f"for i in range (2, -10, -1): {i}")

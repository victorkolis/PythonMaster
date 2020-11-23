# Hide the treasure challenge
# This software objective is emulate a game where a player can hide his treasure a given position in a matrix

row1 = [" ⬜ "," ⬜️ "," ⬜️ "]
row2 = [" ⬜️ "," ⬜️ "," ⬜️ "]
row3 = [" ⬜️ "," ⬜️ "," ⬜ "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

matrix = [row1, row2, row3];
position = input("Where do you want to put the treasure? ")
num1 = int(position[0]) - 1
num2 = int(position[1]) - 1

try:
    matrix[num2][num1] = "x"
    print(f"{row1}\n{row2}\n{row3}")
except:
    print("An exception occured.")

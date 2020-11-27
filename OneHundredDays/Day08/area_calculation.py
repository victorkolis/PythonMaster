# area_calculation.py
# this software objective is to calculate the amount of paint for a given measure of wall

import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def calculate_paint(wall_height, wall_width, coverage):
    amount_of_paint = wall_height * wall_width / coverage
    amount_of_paint = math.ceil(amount_of_paint)
    print(f"You will need {amount_of_paint} cans of paint")
    
calculate_paint(wall_height=test_h, wall_width=test_w, coverage=coverage)

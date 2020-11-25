# average_height_challenge.py

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

average_height = 0
number_of_students = 0

for height in student_heights:
    average_height += student_heights[number_of_students] # or height
    number_of_students += 1
print(average_height // number_of_students)

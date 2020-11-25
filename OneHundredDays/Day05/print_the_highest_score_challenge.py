# print_the_highest_score_challenge.py

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = -1

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is: {highest_score}")

# grading_challenge.py

student_scores = {
  "Edward": 81,
  "Ron": 78,
  "Henry": 99, 
  "Victor": 74,
  "Davis": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"

    elif student_scores[key] >= 81:
        student_grades[key] = "Exeeds Expectations"
        
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
        
    elif student_scores[key] >= 0:
        student_grades[key] = "Fail"
      
print(student_grades)

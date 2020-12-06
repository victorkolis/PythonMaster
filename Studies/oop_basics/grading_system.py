# OOP in Python


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students += [student]

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return round(value / len(self.students), 2)


s1 = Student('Victor', 26, 97)
s2 = Student('Kolis', 26, 99)

course = Course("Python", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.students[1].name)
print(course.get_average_grade())

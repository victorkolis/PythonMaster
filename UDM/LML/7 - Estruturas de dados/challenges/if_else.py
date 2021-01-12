def grading(grade):
    if grade < 0 or grade > 10:
        return 'Invalid grading/value.'
    elif grade >= 9.1:
        return 'A'
    elif grade >= 8.1:
        return 'A-'
    elif grade >= 7.1:
        return 'B'
    elif grade >= 6.1:
        return 'B-'
    elif grade >= 5.1:
        return 'C'
    elif grade >= 4.1:
        return 'C-'
    elif grade >= 3.1:
        return 'D'
    elif grade >= 2.1:
        return 'D-'
    elif grade >= 1.1:
        return 'E'
    else:
        return 'F'


def main():
    print(grading(5))


main()

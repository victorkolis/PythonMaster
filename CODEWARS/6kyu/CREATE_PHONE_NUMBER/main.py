def create_phone_number(n):
    n = [str(number) for number in n]
    phone_number = '('
    for index, number in enumerate(n):
        if index == 3:
            phone_number += ') '
            break
        else:
            phone_number += number

    for number in n[3:6]:
        phone_number += str(number)

    phone_number += '-'
    for number in n[6:11]:
        phone_number += str(number)

    return phone_number


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
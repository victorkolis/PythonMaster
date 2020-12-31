def quarter_of(month):
    if month <= 3:
        return 1
    elif 6 >= month > 3:
        return 2
    elif 9 >= month > 6:
        return 3
    else:
        return 4


print(quarter_of(7))

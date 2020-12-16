while True:
    try:
        number = int(float(input("Please enter a number: ").replace(',', '.')))
        break
    except ValueError:
        pass

print('Thank for entering a number!')

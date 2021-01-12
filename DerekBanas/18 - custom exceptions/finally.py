def divider():
    print('Welcome to the divider')
    num1, num2 = input('Enter two values: ').split()
    try:
        quotient = int(num1) / int(num2)
        print(f'{num1} / {num2} = {quotient}')
    except ZeroDivisionError:
        print('You can\'t divide by zero')

    else:
        print('You did not raise an exception')

    finally:
        print('I execute no matter what!')


def main():
    divider()


main()

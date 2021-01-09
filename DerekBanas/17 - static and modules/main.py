class Add:
    @staticmethod
    def get_addition(*args):
        addition = 0
        for operand in args:
            addition += operand

        return addition


def main():
    print(f'The sum of all the elements entered is {Add.get_addition(1, 2, 3, 4, 5)}')


main()

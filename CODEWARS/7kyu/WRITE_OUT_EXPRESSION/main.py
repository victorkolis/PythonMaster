def expression_out(exp: str) -> str:

    # Pre-declared variables
    fail_message = 'That\'s not an operator!'
    written_expression = ''

    numbers = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
               '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten'}

    symbols = {'*': 'Times', '/': 'Divided By', '+': 'Plus', '-': 'Minus',
               '**': 'To The Power Of', '!=': 'Does Not Equal', '=': 'Equals'}

    # Splitting for character recognition
    exp = exp.split()
    if exp[0] and exp[1] in numbers:
        return fail_message
    else:

        # Getting a hold of the elements in the numbers and symbols dictionaries
        for element in exp:
            if element in numbers:
                written_expression += numbers[element]
            elif element in symbols:
                written_expression += f' {symbols[element]} '
            else:
                return fail_message

        return written_expression


print(expression_out('5 * 4'))

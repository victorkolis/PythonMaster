def to_jaden_case(quote):
    return ' '.join(letter.capitalize() for letter in quote.split())

    # First solution:
    # return quote.title().replace('\'T', '\'t').replace('\'Re', '\'re').replace('\'Ll', '\'ll')\
    #     .replace('\'S', '\'s').replace('\'M', '\'m')


print(to_jaden_case('i am victor kolis'))

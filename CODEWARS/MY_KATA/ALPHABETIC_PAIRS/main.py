__author__ = 'Victor Kolis'


def alphabetic_pairs(string: str, shift: int) -> list:
    string = string.upper()
    if len(string) == 2:
        string = list(string)
        string[0], string[1] = string[1], string[0]
    elif len(string) % 2 != 0:
        string = list(string)
        string.pop(len(string) - 1)

    counter = 0
    alphabet_first_half = list(string[0:len(string) // 2])
    alphabet_second_half = list(string[len(string) // 2:len(string)])

    pairs = []

    while counter != shift:
        for element in alphabet_second_half:
            alphabet_second_half.remove(element)
            alphabet_second_half.append(element)
            break
        counter += 1

    for index in range(len(alphabet_first_half)):
        try:
            pairs += [alphabet_first_half[index] + alphabet_second_half[index]]
        except IndexError:
            pass

    return pairs


print(alphabetic_pairs('CASEsensitive', 4))


# RETIRED KATA, NEEDS IMPROVEMENT

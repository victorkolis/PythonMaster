def solution(string, markers):
    new_string = string.split('\n')
    list_item = ''
    final_string = []
    for index in range(len(new_string)):
        for letter in new_string[index]:
            if letter == markers[0] or letter == markers[1]:
                break
            else:
                list_item += letter
        final_string += [list_item]
        list_item = ''

    return final_string


sentence = '''apples, pears # and bananas\ngrapes\nbananas !apples'''
print(solution(sentence, ['#', '!']))

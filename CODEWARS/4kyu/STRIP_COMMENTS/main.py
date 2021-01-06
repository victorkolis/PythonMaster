def solution(string, markers):
    comment_counter = string.count(markers[0]) + string.count(markers[1])
    for _ in range(2):

        pass
    return 0


sentence = '''apples, pears # and bananas\ngrapes\nbananas !apples'''
print(solution(sentence, ['#', '!']))


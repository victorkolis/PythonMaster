def permutations(sentence):
    sentence = sorted(sentence)
    sentence_list = list(sentence)
    permutation_list = set()
    repetition_counter = 0
    counter = 0
    for index1 in range(len(sentence_list)):
        try:
            sentence_list[0] = sentence_list[index1]
            permutation_list.add(''.join(sentence_list))
        except IndexError:
            pass

        for index2 in range(1, len(sentence_list)):
            try:
                sentence_list[index2], sentence_list[index2 + 1] = sentence_list[index2 + 1], sentence_list[index2]
                permutation_list.add(''.join(sentence_list))
                repetition_counter += 1
            except IndexError:
                pass

        pass
    permutation_list = list(permutation_list)
    permutation_list.sort()
    return permutation_list


print(permutations('abcd'))

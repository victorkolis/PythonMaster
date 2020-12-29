def permutations(sentence):
    if len(sentence) == 1:
        return [sentence]

    permuted = permutations(sentence[1:])
    letter = sentence[0]
    new_sentence = []

    for permutation in permuted:
        for _ in range(len(permutation) + 1):
            new_sentence += [permutation[:_] + letter + permutation[_:]]
    new_sentence = set(new_sentence)
    new_sentence = list(new_sentence)
    new_sentence.sort()
    return new_sentence


print(permutations('abcd'))

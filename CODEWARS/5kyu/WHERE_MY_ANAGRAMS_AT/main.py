def anagrams(word, words):
    word = sorted(word)
    word = ''.join(word)
    anagram_list = []
    for index in range(len(words)):
        anagram = sorted(words[index])
        anagram = ''.join(anagram)
        if anagram == word:
            anagram_list += [words[index]]
        else:
            continue
    return anagram_list


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada', 'baba', 'abab']))

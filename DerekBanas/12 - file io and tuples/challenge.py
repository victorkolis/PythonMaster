with open('my_file.txt', mode='r', encoding='utf-16') as my_file:
    line_number = 0
    while True:
        line = my_file.readline().split()
        number_of_words = len(line)
        line_number += 1
        avg_word_length = 0
        for index in range(len(line)):
            avg_word_length += len(line[index])
        try:
            avg_word_length = round(avg_word_length / number_of_words, 2)
            if '.0' in f'{avg_word_length}':
                avg_word_length = round(avg_word_length)
        except ZeroDivisionError:
            pass
        if not line:
            break
        print(f'Line {line_number}\nNumber of words: {number_of_words}\nAverage word length: {avg_word_length}')

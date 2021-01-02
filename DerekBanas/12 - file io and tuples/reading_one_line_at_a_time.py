with open('my_file.txt', mode='w', encoding='utf-16') as my_file:
    my_file.write('This has been written with a Python script.\nSo did all the other lines.\n************************')

with open('my_file.txt', encoding='utf-16') as my_file:
    line_num = 0
    while True:
        line = my_file.readline()
        line_num += 1
        if not line:
            break
        print('Line :', line_num, ' - ', line, end='')


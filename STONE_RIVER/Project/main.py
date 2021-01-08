import statistics

administrators = {'Victor': '1q2w3e4R'}


def main():
    print('''
    Welcome to grade central
    
    Choose an option
    
    [1] - Enter grades
    [2] - Remove student
    [3] - Student average grades
    [4] - Exit
    ''')

    action = input('What would you like to do today? (Enter an option): ')
    if action == '1':
        pass
    elif action == '2':
        pass
    elif action == '3':
        pass
    elif action == '4':
        pass
    else:
        print('No valid option entered')


login = input('Username: ')
password = input('Password: ')

if login in administrators:
    if administrators[login] == password:
        main()
    else:
        print('Wrong password')

else:
    print('User does not exist!')

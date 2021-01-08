import statistics

administrators = {'Victor': '1q2w3e4R', 'Isaac':'ZSXcfv!#@$#%534231'}


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
        print('Invalid option!')


login = input('Username: ')
password = input('Password: ')
access_message = 'Wrong password or user does not exist'

if login in administrators:
    if administrators[login] == password:
        main()
    else:
        print(access_message)

else:
    print(access_message)

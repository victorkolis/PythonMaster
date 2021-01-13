def is_a_valid_message(message):
    if message == '':
        return True

    elif not message[0].isdigit():
        return False

    else:
        # NOT YET FINISHED
        pass


is_a_valid_message('3 hey 5 hello 2 hi 5')

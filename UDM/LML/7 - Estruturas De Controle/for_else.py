FORBIDDEN_WORDS = ('FOOTBALL', 'RELIGION', 'POLITICS')

texts = [
    'John likes religion and soccer.',
    'The beach was fun.'
]

for text in texts:
    for word in text.upper().split():
        if word in FORBIDDEN_WORDS:
            print('One forbidden word was found!', word)
            break

    else:
        print('Text authorized: ', text)

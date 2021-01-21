FORBIDDEN_WORDS = ('FOOTBALL', 'RELIGION', 'POLITICS')

texts = [
    'John likes religion and soccer.',
    'The beach was fun.'
]

for text in texts:
    found = False
    for word in text.upper().split():
        if word in FORBIDDEN_WORDS:
            print('One forbidden word was found!', word)
            found = True
            break

    if not found:
        print('Text authorized.', text)


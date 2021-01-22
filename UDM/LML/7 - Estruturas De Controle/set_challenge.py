FORBIDDEN_WORDS = {'FOOTBALL', 'RELIGION', 'POLITICS'}

texts = [
    'John likes religion and soccer and politics',
    'The beach was fun.'
]

for text in texts:
    intersection = FORBIDDEN_WORDS.intersection(set(text.upper().split()))
    if intersection:
        print('Forbidden words found:', str(intersection).replace('{', '').replace('}', ''))
    else:
        print('Authorized text: ', text)

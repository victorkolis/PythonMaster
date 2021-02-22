# swap the first letter of the sentences crazy elephant -> erazy clephant

def spoonerize(words):
    # Getting/Separating the word in the string
    first_word = list(words.split()[0])
    second_word = list(words.split()[1])
    
    # Swap
    first_word[0], second_word[0] = second_word[0], first_word[0]  
    
    
    return f"{''.join(first_word)} {''.join(second_word)}"


print(spoonerize('Victor Kolis'))


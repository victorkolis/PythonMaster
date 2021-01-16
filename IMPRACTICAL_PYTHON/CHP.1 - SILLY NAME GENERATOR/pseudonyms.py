import random
import subprocess
import time
from termcolor import TermColor

print('Welcome to the Psych \'Sidekick Name Picker.\'')
print('A name just like Sean would pick for Gus:\n\n')

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
         "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ", 'Butterbean',
         'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy', 'Chigger", "Cinnabuns',
         'Cleet', 'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer',
         'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim',
         'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
         'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"',
         'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
         'Potato Bug', 'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
         "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
         'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
         "Winston 'Jazz Hands'", 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout',
        'Butterbaugh', 'Clovenhoof', 'Clutterbuck', 'Cocktoasten', 'Endicott',
        'Fewhairs', 'Gooberdapple', 'Goodensmith', 'Goodpasture', 'Guster', 'Henderson',
        'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt',
        'Johnson', 'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler',
        'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins', 'Putney',
        'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine',
        'Splern', 'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners',
        'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')


while True:
    first_name = random.choice(first)
    last_name = random.choice(last)

    time.sleep(1)
    subprocess.call('clear')
    print(TermColor().random_color, '\n{} {}'.format(first_name, last_name), TermColor().reset_color)
    try:
        try_again = input('\n\nTry again? (Press Enter else n to quit)\n')
        if try_again.lower() == 'n':
            subprocess.call('clear')
            break

    except TypeError:
        pass

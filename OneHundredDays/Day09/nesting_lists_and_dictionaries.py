# nesting_lists_and_dictionaries.py

# List nesting
chords_notes = {
    'C':['C', 'E', 'G'],
    'G':['G', 'B', 'D'],
    }

# Dicitonary nesting
chords_notes = {
    'C':['C', 'E', 'G'],
    
    'G':{'G': ['G', 'B', 'D'],
         'A': ['A', 'C#', 'E']
        },
    }
print(chords_notes)

# Nesting dictionary in a list

chords_notes = [
    {'Major Scales': {'C':['DO', 'MI', 'SOL']},
     
    },
    
    {'Major Scales': {'G':['SOL', 'TI', 'RE']},
     'Major Scales': {'A': ['A', 'C#', 'E']}}
    ]

print(chords_notes[1])

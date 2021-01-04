class Animal:
    def __init__(self, animal_type='', name=''):
        self.eyes = 2
        self.name = name.title()
        self.animal_type = animal_type

    def breath(self):
        if self.name != '' and self.animal_type != '':
            print('{} the {} is breathing.'.format(self.name, self.animal_type.lower()))

        elif self.animal_type == '':
            print('The animal is breathing.')

        else:
            print('The {} is breathing.'.format(self.animal_type.lower()))

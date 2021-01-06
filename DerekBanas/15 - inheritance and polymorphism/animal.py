class Animal:
    def __init__(self, birth_type='Unknown', appearance='Unknown', blooded='Unknown'):
        self.__birth_type = birth_type
        self.__appearance = appearance
        self.__blooded = blooded

    # birth_type getter
    @property
    def birth_type(self):
        return self.__birth_type

    # birth_type setter
    @birth_type.setter
    def birth_type(self, birth_type):
        self.__birth_type = birth_type

    # blooded getter
    @property
    def blooded(self):
        return self.__blooded

    # blooded setter
    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    # appearance getter
    @property
    def appearance(self):
        return self.__appearance

    # nurse_young setter
    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    # To string
    def __str__(self):
        return "A {} is {} it has {} it is {}.".format(type(self)
                                                      .__name__, self.birth_type, self.appearance, self.blooded)


class Mammal(Animal):
    def __init__(self, birth_type='born alive', appearance='hair or fur', blooded='warm blooded', nurse_young=True):
        Animal.__init__(self, birth_type, appearance, blooded)
        self.__nurse_young = nurse_young

    # nurse_young getter
    @property
    def nurse_young(self):
        return self.__nurse_young

    # blooded setter
    @nurse_young.setter
    def nurse_young(self, nurse_young):
        self.__nurse_young = nurse_young

    def __str__(self):
        return super().__str__() + " And it is {} they nurse their young".format(self.nurse_young)


class Reptile(Animal):
    def __init__(self, birth_type='born in egg or born alive', appearance='dry scales', blooded='cold blooded'):
        Animal.__init__(self, birth_type, appearance, blooded)


def main():
    animal_1 = Animal('born alive')
    print(animal_1)
    mammal_1 = Mammal()
    print(mammal_1)
    reptile = Reptile()
    print(reptile)


main()

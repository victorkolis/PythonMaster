from animal import *


class Cat(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print('Through snout.')

    @staticmethod
    def lick():
        print('Licking fur...')

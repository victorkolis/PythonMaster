from animal import *


class Bird(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print('Through beak holes.')

    @staticmethod
    def fly():
        print('Flying...')

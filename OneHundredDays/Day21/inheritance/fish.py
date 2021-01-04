from animal import *


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print('Through gills.')

    @staticmethod
    def swim():
        print('Swimming...')

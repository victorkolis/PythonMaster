import random
import math


class Warrior:
    def __init__(self, name='Warrior', health=0, attack_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attack_max = attack_max
        self.block_max = block_max

    def attack(self):
        attack_amount = self.attack_max * (random.random() + .5)
        return attack_amount

    def block(self):
        block_amount = self.block_max * (random.random() + .5)
        return block_amount


def get_attack_result(warrior_a, warrior_b):
    warrior_a_attack_amount = warrior_a.attack()
    warrior_b_block_amount = warrior_b.block()
    damage_to_warrior_b = math.ceil(warrior_a_attack_amount - warrior_b_block_amount)
    warrior_b.health = warrior_b.health - damage_to_warrior_b
    print("{} attacks {} and deals {} damage".format(warrior_a.name, warrior_b.name, damage_to_warrior_b))
    print("{} is down to {} health".format(warrior_b.name, warrior_b.health))

    if warrior_b.health <= 0:
        print('{} has died and {} is victorious'.format(warrior_b.name, warrior_a.name))
        return 'Game over'
    else:
        pass


def start(warrior1, warrior2):
    while True:
        if get_attack_result(warrior1, warrior2) == 'Game over':
            break

        elif get_attack_result(warrior2, warrior1) == 'Game over':
            break


class Battle:
    pass


def main():
    suit = Warrior('Suit', 50, 20, 10)
    player = Warrior('Player', 50, 20, 10)
    start(suit, player)


main()

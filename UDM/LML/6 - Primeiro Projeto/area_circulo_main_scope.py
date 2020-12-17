#!/usr/local/bin/python3

from math import pi

if __name__ == '__main__':
    raio = float(input('Insira o valor do raio: '))
    print("Área do círculo", round(pi * raio ** 2, 2))

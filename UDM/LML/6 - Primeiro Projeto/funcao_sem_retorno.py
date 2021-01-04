#!/usr/local/bin/python3
from math import pi


def circulo(raio):
    print("Área do círculo", round(pi * raio ** 2, 2))


if __name__ == '__main__':
    raio = float(input('Insira o valor do raio: '))
    circulo(raio)

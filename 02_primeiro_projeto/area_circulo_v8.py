#!/usr/local/bin/python3
from math import pi

def circulo(raio):
    print(f"Área do círculo {(pi * float(raio) ** 2):.2f}")

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)

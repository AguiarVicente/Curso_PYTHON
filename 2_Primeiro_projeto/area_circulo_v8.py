#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import math


def circulo(raio):
    print('Area do circulo ', math.pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Digite o raio: ')
    circulo(raio)

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import math
import sys


def circulo(raio):
    return math.pi * float(raio) ** 2


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do circulo', area)

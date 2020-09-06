#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import math
import sys
import errno


def circulo(raio):
    return math.pi * float(raio) ** 2


def help():
    print("É necessário informar o raio do círculo")
    print(f"Sintaxe: {sys.argv[0][2:]} <raio>")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor numérico')
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do circulo', area)

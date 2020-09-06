#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import math
import sys
import errno


class TerminalColor:
    ERRO = '\033[1;41m \033[1;97m'
    NORMAL = '\033[0m'


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
        print(TerminalColor.ERRO +
              'O raio deve ser um valor numérico' + TerminalColor.NORMAL)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do circulo', area)

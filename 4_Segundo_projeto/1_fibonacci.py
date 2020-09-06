# !/usr/local/bin/python3
# -*- coding: utf-8 -*-
def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}')
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci()

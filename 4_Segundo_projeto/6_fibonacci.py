# !/usr/local/bin/python3
# -*- coding: utf-8 -*-
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)

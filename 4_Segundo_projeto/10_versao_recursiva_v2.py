# !/usr/local/bin/python3
def fibonacci(quantidade, sequiencia=(0, 1)):
    # condição de parada
    return sequiencia if len(sequiencia) == quantidade else \
        fibonacci(quantidade, sequiencia + (sum(sequiencia[-2:]), ))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)

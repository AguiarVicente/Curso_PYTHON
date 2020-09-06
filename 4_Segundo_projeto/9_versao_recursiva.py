# !/usr/local/bin/python3
def fibonacci(quantidade, sequiencia=(0, 1)):
    if len(sequiencia) == quantidade:
        return sequiencia
    return fibonacci(quantidade, sequiencia + (sum(sequiencia[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)

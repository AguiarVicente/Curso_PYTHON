# !/usr/local/bin/python3

def fibonacci(sequiencia=None):
    sequiencia = sequiencia or [0, 1]
    sequiencia.append(sequiencia[-1] + sequiencia[-2])
    return sequiencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]

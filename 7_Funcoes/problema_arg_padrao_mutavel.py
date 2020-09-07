# !/usr/local/bin/python3

def fibonacci(sequiencia=[0, 1]):
    # uso de mutaveis como valor default (armadilha)
    sequiencia.append(sequiencia[-1] + sequiencia[-2])
    return sequiencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]

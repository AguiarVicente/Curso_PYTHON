# !/usr/local/bin/python3
class Animal:
    @property
    def capacidade(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidade(self):
        return super().capacidade + ('amar', 'falar', 'estudar')


class Aranha(Animal):
    @property
    def capacidade(self):
        return super().capacidade + ('fazer teia', 'andar pelas paredes')


class HomemAranha(Homem, Aranha):
    @property
    def capacidade(self):
        return super().capacidade + \
            ('bater em bandidos', 'atirar teias entre prédios')


if __name__ == '__main__':
    jhon = Homem()
    print(f'John: {jhon.capacidade}')

    aranha = Aranha()
    print(f'aranha: {aranha.capacidade}')

    peter = HomemAranha()
    print(f'Peter Parker: {peter.capacidade}')

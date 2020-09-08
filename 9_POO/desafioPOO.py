# !/usr/local/bin/python3
from datetime import datetime
from functools import reduce

MaiorIdade = 18


class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        if not self.idade:
            return self.nome

    def is_adulto(self):
        if self.idade > 18:
            return (self.idade or 0) > MaiorIdade


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(self, nome, idade, salario)
        self.salario = salario


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(self, nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        return None if not self.compras else sorted(self.compras,
                                                    key=lambda compra:
                                                    compra.data)[-1].data

    def total_compras(self):
        return reduce(lambda c1, c2: c1 + c2, (compra.valor for
                                               compra in self.compras))


class Compra(object):
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = datetime.now()
        self.valor = valor

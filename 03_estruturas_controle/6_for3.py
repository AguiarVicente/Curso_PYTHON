#!/usr/local/bin/python3
produto = {'nome': 'Caneta chic', 'preco': 14.99, 'imprtada': True, 'estoque': 793}

for chave in produto:
  print(chave)

for valor in produto.values():
  print(valor)

for chave, valor in produto.items():
  print(chave, '=', valor)

print(chave, valor) # são variáveis globais mesmo delcaradas dentro de um laço
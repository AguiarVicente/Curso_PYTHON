#!/usr/local/bin/python3
#Desafio usando o set

PALABRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
  'João gosta de futebol e política',
  'A praia foi divertida'
]

for texto in textos:
  intersecao = PALABRAS_PROIBIDAS.intersection(set(texto.lower().split()))
  if intersecao:
    print(f'Texto possui pelo menos uma palavra proíbida: {intersecao}')
  else:
    print(f'Texto autorizado: {texto}')
#!/usr/local/bin/python3
#criando uma constante (apenas convenção) - usar letras maiúsculas
PALABRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
  'João gosta de futebol e política',
  'A praia foi divertida'
]

for texto in textos:
  for palavra in texto.lower().split():
    if palavra in PALABRAS_PROIBIDAS:
      print(f'Texto possui pelo menos uma palavra proíbida: {palavra}')
      break
  else:
    print(f'Texto autorizado: {texto}')

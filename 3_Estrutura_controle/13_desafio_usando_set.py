PALAVRAS_PROIBIDAS = {'futebol', 'Religião', 'política'}
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possoui palavras príbidas', intersecao)
    else:
        print('Texto autorizado: ', texto)

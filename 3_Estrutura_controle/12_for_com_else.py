PALAVRAS_PROIBIDAS = ('futebol', 'Religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possoui pelo menos uma palavra príbida:', palavra)
            break
    else:
        print('Texto autorizado', texto)

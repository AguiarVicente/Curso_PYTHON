PALAVRAS_PROIBIDAS = ('futebol', 'Religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possoui pelo menos uma palavra príbida:', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado', texto)

# !/usr/local/bin/python3

'''
Conceitos
A de 10,0 à 9,1
-A de 9,0 à 8,1
B de 8,0 à 7,1
-B de 7,0 à 6,1
C de 6,0 à 5,1
-C de 5,0 à 4,1
D de 4,0 à 3,1
-D de 3,0 à 2,1
E de 2,0 à 1,1
-E de 1,0 à 0,0

Para notas maiores que 10 e monires que 0 será impressp "Nota inválida"
'''


def nota_conceito(valor):
    if valor.isnumeric():
        nota = float(valor)
    else:
        return 'Digite um valor numérico'

    if nota > 10:
        return 'Nota inválida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0.0:
        return 'E-'
    else:
        return 'Nota inválida'


if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)

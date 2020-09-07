# !/usr/local/bin/python3
def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana',
    }
    dia_ecolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_ecolhido, '** dia inválido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')

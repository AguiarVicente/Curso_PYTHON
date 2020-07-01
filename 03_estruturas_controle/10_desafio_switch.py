#!/usr/local/bin/python3

def get_tipo_dia(dia):
  dias = {
    1: 'Fim de semama',
    2: 'Dia de semama',
    3: 'Dia de semama',
    4: 'Dia de semama',
    5: 'Dia de semama',
    6: 'Dia de semama',
    7: 'Fim de semama'
  }
  return dias.get(dia, '** inválido **')

if __name__ == '__main__':
  for dia in range(0, 9):
    print(f'{dia} - {get_tipo_dia(dia)}')
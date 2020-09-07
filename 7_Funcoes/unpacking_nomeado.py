# **kwargs
def resultado_f1(primeiro, segundo, terceito):
    print(f'1) -> {primeiro}')
    print(f'2) -> {segundo}')
    print(f'3) -> {terceito}')


if __name__ == '__main__':
    podium = {'primeiro': 'L. Hamilton',
              'segundo': 'M. Verstappen',
              'terceito': 'S. Vettel'}
    resultado_f1(**podium)

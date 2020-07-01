#!/usr/local/bin/python3
from random import randint


for i in range(1, 10):
  if i == 6:
    break
  print(i)
else:
  print('Fim!')

# Função sortear_dado numeros entre 1 e 6
# for com range 1 a 6
# se for ímpar continue
# se o numero for para e for igual ao valor sorteado
# pela função dado, imprimir 'ACERTOU'e depois chamar o creak
# Se náo acertar chama o else... print('Não acertou o número)

# for e else
def sortear_dado():
  return randint(1, 6)

for i in range(1, 7):
  if i % 2 == 1:
    continue
  if sortear_dado() == i:
    print('ACERTOU', i)
    break
else:
  print('NÃO ACERTOU')
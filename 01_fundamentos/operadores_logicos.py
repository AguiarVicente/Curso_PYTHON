# operadores lógicos
print(True or False)
print(7 != 3 and 2 > 3)

# tabela verdade do AND
print('Tabela verada de AND')
print( True and True )
print( True and False )
print( False and True )
print( False and False )

# tabela verdade do OR
print('Tabela verada de OR')
print( True or True )
print( True or False )
print( False or True )
print( False or False )

# Tabela verdade do xor
print('Tabela verada de XOR')
print( True != True )
print( True != False )
print( False != True )
print( False != False )

# tabela verdade NOT
print('Operador Negacao')
print( not True )
print( not False )
print( not 1 )
print( not 0 )

# cuidade ( operador bit a bit )
print('Operador BIT a BIT')
print( True & True )
print( False | True )
print( True ^ True )

print('AND bit a bit')
print( 3 & 2 )

print('OR bit a bit')
print( 3 | 3 )

print('XOR bit a bit')
print( 3 ^ 2 )

# um pouco de realidade
saldo = 1000
salario = 4000
despesas = 2967
meta = saldo > 0 and salario - despesas >= 0.2 * salario
print( meta )

saldo = 1000
salario = 4000
despesas = 3900
meta = saldo > 0 & salario - despesas >= 0.2 * salario
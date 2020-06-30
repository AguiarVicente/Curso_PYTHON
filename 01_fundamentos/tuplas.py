# tuplas

tupla = tuple()
tupla1 = ()
print(type(tupla))
print(type(tupla1))
# print(help(tuple))

tupla2 = ('um')
print(type(tupla2))

# forma correta de declarar uma tupla com um elemento apenas
tuplaC = ('um', )
print(tuplaC)

cores = ('verde', 'amarelo', 'azul')
print(cores)
print(cores[0])
print(cores[-1])
print(cores[1:])
print(cores.index('amarelo'))
print(cores.count('amarelo'))
print(len(cores))
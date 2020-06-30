# conjuntos (set) - não indexado - não aceita repetição de valores - não garante ordenação
# conjuntos = { valores }
conjunto = {1, 2, 3}
print(type(conjunto))
conjunto = set('Cod3r')
print(conjunto)
print('3' in conjunto, 'C' not in conjunto)

c1 = {1, 2}
c2 = {2, 3}

#união
print(c1.union(c2))

# interseção
print(c1.intersection(c2))

# c1.update(c2)
print(c1)

# subconjunto
print(c2 <= c1)

# superconjunto
print(c1 >= c2)

print({1,2,3} - {2})

print(c1 - c2)
c1 -= {2}
print(c1)
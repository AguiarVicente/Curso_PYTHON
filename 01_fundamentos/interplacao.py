from string import Template
# interpolar string (4 formas)

# forma 1 - mais antiga
nome, idade = 'Ana', 30.9875
print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: %s Idade: %.2f' % (nome, idade))
print('Nome: %s Idade: %.2f %r' % (nome, idade, True))

# forma 2
print('Nome: {0} Idade: {1}'.format(nome, idade))

# forma 3
print(f"Nome: {nome} Idade: {idade:.2f} {2 ** 8}")

# forma 4
s = Template('Nome: $nome Idade: $idade') # necessario importar string de Template

print(s.substitute(nome=nome, idade=idade))
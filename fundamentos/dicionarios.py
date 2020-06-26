# Dictionary -> parecido com objeto em JS porém não é objeto em Python
# nome = { 'chave': 'valor' }
# print(help(dict))
pessoa = {'nome': 'Nil', 'idade': 34, 'curso': ['Python', 'Angular']}
print(type(pessoa))
print(len(pessoa))
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['curso'][1])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.get('idade'))
print(pessoa.get('curso'))
print(pessoa.get('nome'))

# parte 2
nova_pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
nova_pessoa['idade'] = 44
nova_pessoa['cursos'].append('Angular')
print(nova_pessoa)

nova_pessoa.pop('idade')
print(nova_pessoa)
nova_pessoa.update({'idade': 40, 'Sexo': 'M'})
print(nova_pessoa)

del nova_pessoa['cursos']
print(nova_pessoa)

nova_pessoa.clear()
print(nova_pessoa)
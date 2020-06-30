# tipo string
# print(dir(str))

nome = 'Saulo Pedro'
print(nome)
print(nome[0])
print(nome.replace(r'S', 'P'))

b = 'marca d\'água'
# ou
b = "marca d'água"
print(b)

c = """Texto com
...multiplas linhas"""

print(c)

d = 'quebrando linha \ncom \\n'
print(d)

e = '\t tab'
print(e)

nome1 = 'Ana Paula'
print(nome1[0], nome1[6], nome1[-3], nome1[4:], nome1[-5:], nome1[:3], nome1[2:5])

numeros = '1234567890'
print(numeros)
print(numeros[:])
print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])
print(numeros[::-2])

print(nome1[::-1])

# operador membro no contexto de string
frase = 'Python é uma linguagem estremamente fácil de aprender'
print('Py' in frase) # true
print(frase.lower())
print('py' in frase) # false
print(frase.upper())
print(frase)
print(frase.split())
print(frase.split('a'))

# métodos mágicos
# Magic Method 

stringA = '123'
stringB = ' de oliveira 4'
print(stringA + stringB)
print(stringA.__add__(stringB))
print(len(stringA))
print(len(stringB))
print(stringA.__contains__('1'))
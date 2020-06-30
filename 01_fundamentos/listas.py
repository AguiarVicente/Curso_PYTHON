# listas (array)
lista = []
lista.append(1) # altera a lista
print(lista)
print(len(lista))

nova_lista = [1, 2, 3, 4, 5]
nova_lista.remove(5) # altera a lista
print(nova_lista)
nova_lista.reverse() # altera a lista
print(nova_lista)

# parte 2
lista_parte = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
print(lista_parte.index('Guilherme'))
print(lista_parte[2])
print('Rebeca' in lista_parte)
print(lista_parte[4])
print(lista_parte[-1])
print(lista_parte[-5])

# parte 3
outra_lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(outra_lista[1:3])
print(outra_lista[1:-1])
print(outra_lista[1:])
print(outra_lista[:-1])
print(outra_lista[:])
print(outra_lista[::2])
print(outra_lista[::-1])

del outra_lista[1]
print(outra_lista)
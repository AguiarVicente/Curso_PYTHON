# Builtins e escopo global
print(type(1)) 
print(__builtins__.type('Fala Galera!'))
__builtins__.print(10 / 3)
# print(__builtins__.help(__builtins__.dir))

a = 10
print(dir())
print(dir(__builtins__))
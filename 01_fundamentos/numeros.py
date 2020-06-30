# tipos numericos
# print(dir(int))
# print(dir(float))

a = 5
b = 2.5

print(a / b)
print(a + b)
print(a * b)

print(b.is_integer())
print((-2).__abs__()) # 2
print(abs(-20)) # 20

# decimal
print(1.1 + 2.2)

from decimal import Decimal, getcontext
print(Decimal(1.1) + Decimal(2.2))
getcontext().prec = 4
print(Decimal(1.1) + Decimal(2.2))

getcontext().prec = 10
print(Decimal(1.1) + Decimal(2.2))

print(dir(Decimal))
print(dir(getcontext))
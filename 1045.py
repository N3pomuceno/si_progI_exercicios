lados = input().split()
a = float(lados[0])
b = float(lados[1])
c = float(lados[2])

if (b > a)and(b > c):
    d = b
    b = a
    a = d
elif (c > a)and(c > b):
    d = c
    c = a
    a = d

if (a >= b + c):
    print('NAO FORMA TRIANGULO')
elif (a ** 2 == b ** 2 + c ** 2):
    print('TRIANGULO RETANGULO')
elif (a ** 2 > b ** 2 + c ** 2):
    print('TRIANGULO OBTUSANGULO')
elif (a ** 2 < b ** 2 + c ** 2):
    print('TRIANGULO ACUTANGULO')
else:
    print()
if (a == b)and(a == c):
    print('TRIANGULO EQUILATERO')
elif (a == b)and(a != c):
    print('TRIANGULO ISOSCELES')
elif (a != b)and(a == c):
    print('TRIANGULO ISOSCELES')
elif (c == b)and(a != c):
    print('TRIANGULO ISOSCELES')
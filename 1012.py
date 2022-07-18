#area
valores = input().split()
PI = 3.14159
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

areaTriangulo = (a * c) / 2
areaCirculo = PI * c ** 2
areaTrapezio = ((a + b) * c) / 2
areaQuadrado = b ** 2
areaRetangulo = a * b

""" gerou erro no URI
print('''
TRIANGULO: {:.3f}
CIRCULO: {:.3f}
TRAPEZIO: {:.3f}
QUADRADO: {:.3f}
RETANGULO: {:.3f}
'''.format(areaTriangulo,areaCirculo,areaTrapezio,areaQuadrado,areaRetangulo))
"""
print("TRIANGULO: {:.3f}".format(areaTriangulo))
print("CIRCULO: {:.3f}".format(areaCirculo))
print("TRAPEZIO: {:.3f}".format(areaTrapezio))
print("QUADRADO: {:.3f}".format(areaQuadrado))
print("RETANGULO: {:.3f}".format(areaRetangulo))
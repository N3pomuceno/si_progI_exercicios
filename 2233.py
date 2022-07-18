# Programa
"""
1fa8
3bc
12

fffff0
ffffff
ab2c1

ffffff
1
1
"""

# Principal
larguraVerm = int(input(), 16)
larguraVerd = int(input(), 16)
larguraAzul = int(input(), 16)

qtdVerm = 1
qtdVerd = larguraVerm//larguraVerd
qtdAzul = larguraVerd//larguraAzul

resultado = (qtdVerm+((qtdVerd)**2)+((qtdVerd)**2)*((qtdAzul)**2))
print('{:x}'.format(resultado))




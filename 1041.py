ponto = input().split()
x1 = float(ponto[0])
y1 = float(ponto[1])

if (x1 > 0) and (y1 > 0):
    print('Q1')
elif (x1 < 0) and (y1 > 0):
    print('Q2')
elif (x1 < 0) and (y1 < 0):
    print('Q3')
elif (x1 > 0) and (y1 < 0):
    print('Q4')
elif (x1 == 0) and (y1 != 0):
    print('Eixo Y')
elif (x1 != 0) and (y1 == 0):
    print('Eixo X')
else:
    print('Origem')
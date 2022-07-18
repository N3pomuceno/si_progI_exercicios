'''
valores = input().split()
valores = list(map(float,valores)
a = valores[0]
b = valores[1]
c = valores[2]

'''

a,b,c = list(map(float, input().split()))
delta = b ** 2 - 4 * a * c
if (delta >= 0)and(a != 0):
    r1 = (- b + (delta) ** (1/2))/(2 * a)
    r2 = (- b - (delta) ** (1/2))/(2 * a)
    print ("R1 = {:.5f}".format(r1))
    print ("R2 = {:.5f}".format(r2))
else:
    print("Impossivel calcular")
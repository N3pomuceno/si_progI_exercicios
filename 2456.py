#Programa

#Subprogramas
def ordenacao(car, num):
    if num == 1:
        for ind in range(1, len(car)):
            if car[ind] < car[ind-1]:
                return False
    elif num == 2:
        for ind in range(1, len(car)):
            if car[ind] > car[ind-1]:
                return False
    return True

#Principal
cartas = list(map(int,input().split()))
crescente = ordenacao(cartas, 1)
decrescente = ordenacao(cartas, 2)

if crescente:
    print("C")
elif decrescente:
    print("D")
else:
    print("N")

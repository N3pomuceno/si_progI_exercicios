#Programa

#Subprograma

#Principal
numeroDeRodadas = int(input())
while numeroDeRodadas != 0:

    vit1 = vit2 = 0
    for ind in range(numeroDeRodadas):
        num1, num2 = map(int, input().split())
        if num1 > num2:
            vit1+=1
        elif num2 > num1:
            vit2+=1

    print("{} {}".format(vit1, vit2))

    numeroDeRodadas = int(input())


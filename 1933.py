#Programa

#principal

carta1, carta2 = map(int, input().split())
if carta1 == carta2:
    print(carta1)
else:
    if carta1 > carta2:
        print(carta1)
    elif carta2 > carta1:
        print(carta2)


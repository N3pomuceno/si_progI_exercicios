lista = input().split()
a1 = int(lista[0])
a2 = int(lista[1])
a3 = int(lista[2])

if (a1 < a2) and (a1 < a3):
    menor = a1
    if (a2 < a3):
        meio = a2
        maior = a3
    else:
        meio = a3
        maior = a2
elif (a2 < a1) and (a2 < a3):
    menor = a2
    if (a1 < a3):
        meio = a1
        maior = a3
    else:
        meio = a3
        maior = a1
else:
    menor = a3
    if (a1 < a2):
        meio = a1
        maior = a2
    else:
        meio = a2
        maior = a1
print(menor)
print(meio)
print(maior)
print()
print(a1)
print(a2)
print(a3)

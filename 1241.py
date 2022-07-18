# programa



# Principal
numDeCasos = int(input())

for ind in range(numDeCasos):
    a, b = input().split()
    if a[len(a)-len(b):] == b:
        print("encaixa")
    else:
        print("nao encaixa")

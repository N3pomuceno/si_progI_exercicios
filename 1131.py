nGrenal = 1
inter = gremio = empate = grenal = 0

while nGrenal == 1:
    a , b = list(map(int,input().split()))
    grenal = grenal + 1
    if a > b:
        inter = inter + 1
    elif b > a:
        gremio = gremio + 1
    else:
        empate = empate + 1
    print("Novo grenal (1-sim 2-nao)")
    nGrenal = int(input())

print("{} grenais".format(grenal))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empate))
if inter > gremio and inter > empate:
    print("Inter venceu mais")
elif gremio > inter and gremio > empate:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")

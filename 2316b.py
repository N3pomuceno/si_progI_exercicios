# Programa
# subprogramas
def verificacao(k, c, s, inf):
    carro = localizaCarro(inf, c)
    if s == inf[carro][1] + 1:
        inf[carro][1] = s
    if inf[carro][1] == k:
        inf[carro][1] = 0
        inf[carro][2] += 1

    voltas = inf[c-1][2]
    temp = inf[carro]
    inf.pop(carro)
    inf.insert(posicaoMenor(inf, s, voltas), temp)
    return None

def localizaCarro(inf, c):
    pos = 0
    for i in range(len(inf)):
        if inf[i][0] == c:
            pos = i
    return pos

def posicaoMenor(inf, s, v):
    pos = 0
    for i in range(len(inf)):
        if info[i][1] == s and info[i][2] == v:
            pos = i+1
    return pos

def funf(inf):
    carro, sensor, voltas = inf
    return voltas, sensor

#principal
k, n, m = map(int, input().split()) #postos, carros, leituras
info = [None]*n
for i in range(n):
    info[i] = [i+1, 0, 0] #Identificação do carro, último sensor, quantidade de voltas
for j in range(m):
    car, sen = map(int, input().split())
    verificacao(k, car, sen, info)

info.sort(key=funf, reverse=True)

# print(info)
#for pos in range(len(info)):
#    print("{} ".format(info[pos][0]), end="")

resultado = ""
for i in range(len(info)):
    resultado += str(info[i][0])+" "
print(resultado.rstrip())

#Programa Matring



#Subprogramas
def armazenamento(f, m, l, linha):
    f[0] += linha[0]
    for ind in range(1, len(linha)-1):
        m[ind-1]+=linha[ind]
    l[0] += linha[len(linha)-1]
    return None


def decodificacao(f,m,l):
    resultado=""
    for ind in range(len(m)):
        resultado += chr((int(f[0])*int(m[ind])+int(l[0]))% 257)
    print(resultado)
    return None

#Principal

for ind in range(4):
    linha=input()
    if ind == 0:
        F = [""]
        M = [""]*(len(linha)-2)
        L = [""]
    armazenamento(F, M, L, linha)
decodificacao(F, M, L)


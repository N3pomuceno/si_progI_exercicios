#Programa
#Subprogramas
def operacao(mat, col, defin):
    resultado = 0
    if defin == "S":
        for linha in mat:
            resultado += linha[col]
        print("{:.1f}".format(resultado))
    elif defin == "M":
        for linha in mat:
            resultado += linha[col]
        resultado /= 12
        print("{:.1f}".format(resultado))
    return None


#Programa
colunaDeOperacao = int(input())
definicaoDeOperacao = input()

#criação de matriz
matriz = []
for linha in range(12):
    novaLinha = []
    for coluna in range(12):
        num = float(input())
        novaLinha.append(num)
    matriz.append(novaLinha)

operacao(matriz, colunaDeOperacao, definicaoDeOperacao)

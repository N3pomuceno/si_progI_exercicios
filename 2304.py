#Programas

#Subprogramas
def reacao(acao, cont):
    if acao[0] == "C":
        controle[onde(acao[1], controle)][1] -= int(acao[2])
    elif acao[0] == "V":
        controle[onde(acao[1], controle)][1] += int(acao[2])
    elif acao[0] == "A":
        controle[onde(acao[1], controle)][1] += int(acao[3])
        controle[onde(acao[2], controle)][1] -= int(acao[3])
    return None

def onde(text, controle):
    for posicao in range(len(controle)):
        if text == controle[posicao][0]:
            pos = posicao
    return pos

#principal
dinheiroInicial, numDeRodadas = map(int, input().split())
controle = [["D", dinheiroInicial], ["E", dinheiroInicial], ["F", dinheiroInicial]]
for ind in range(numDeRodadas):
    acao = list(input().split())
    reacao(acao, controle)

print("{} {} {}".format(controle[0][1], controle[1][1], controle[2][1]))


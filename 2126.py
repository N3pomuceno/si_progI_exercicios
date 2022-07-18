#Program

#Subs
def impressao(c, p):
    if contagem == 0:
        print("Nao existe subsequencia")
    else:
        print("Qtd.Subsequencias: {}".format(c))
        print("Pos: {}".format(p + 1))
    print()
    return None

#Principal
cont = 1
while True:
    try:
        sub = input()
        seq = input()
        contagem = 0
        for pos in range(len(seq)):
            if seq[pos: len(sub)+pos] == sub:
                contagem += 1
                posicao = pos
        print("Caso #{}:".format(cont))
        impressao(contagem, posicao)
        cont += 1

    except EOFError:
        break
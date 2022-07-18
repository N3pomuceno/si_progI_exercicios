inicio, fim = list(map(int, input().split()))
if (inicio > fim):
    total = fim + 24 - inicio
    print('O JOGO DUROU {} HORA(S)'.format(total))
elif (inicio < fim):
    total = fim - inicio
    print('O JOGO DUROU {} HORA(S)'.format(total))
else:
    total = 24
    print('O JOGO DUROU {} HORA(S)'.format(total))
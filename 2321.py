# programa


#Principal

Q1P1x, Q1P1y, Q1P2x, Q1P2y = map(int, input().split())
Q2P1x, Q2P1y, Q2P2x, Q2P2y = map(int, input().split())

#Trabalhando interseção por eixo
# Pensar em uma dimensão é mais fácil, com linhas, a linha mais da direita tem que ter seu ponto esquerdo menor ou igual ao ponto direito da linha mais a esquerda.
# e o ponto mais a direita tem que maior ou igual ao ponto mais a esquerda da linha mais a esquerda, é isso que está abaixo (é mais fácil desenhar).
#Eixo X
interX = Q1P2x >= Q2P1x and Q1P1x <= Q2P2x
#Eixo Y
interY = Q1P2y >= Q2P1y and Q1P1y <= Q2P2y

if interX and interY:
    print(1)
else:
    print(0)


notas = input().split()
#notas = list(map(float,notas)) normalmente seria isso que eu faria seguido de varias variaveis sendo partes dessa lista
#EUREKA CARALHO
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])
media = (2 * n1 + 3 * n2 + 4 * n3 + n4)/ 10
if media >= 7.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media >= 5.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    n5 = float(input())
    novaMedia = (n5 + media)/ 2
    print('Nota do exame: {:.1f}'.format(n5))
    if novaMedia >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(novaMedia))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(novaMedia))
else:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
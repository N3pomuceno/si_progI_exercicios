'''
def linguagem(num):
    lingua = input()
    if num == 1:
        return lingua
    for i in range(2,num):
        lingua2 = input()
        if lingua != lingua2:
            return "inglês" #errado pois retorna o resultado mais rápido que o necessário

    return lingua
'''

def linguagem(num):
    lingua = input()
    c = 0
    if num == 1:
        return lingua
    for i in range(2,num+1):
        lingua2 = input()
        if lingua != lingua2:
            c = 1
    if c == 0:
        return lingua
    else:
        return "ingles"

valor = int(input())
for i in range(valor):
    numDePessoas = int(input())
    print(linguagem(numDePessoas))
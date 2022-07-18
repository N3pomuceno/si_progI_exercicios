#Programa
#Subprogramas
"""
4
Top Coder comp Wedn at midnight
one three five
I love Cpp
sj a sa df r e w f d s a v c x z sd fd
as ae df s a w df aw cv fds

"""



#Principal
numDeCasos = int(input())

for ind in range(numDeCasos):
    frase = list(input().split())
    frase.sort(key=len, reverse=True)

    texto = ""
    for jnd in range(len(frase)):
        texto += frase[jnd] + " "
    texto = texto[0:len(texto) - 1]
    print(texto)

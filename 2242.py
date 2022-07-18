#programa
#Subprograma
def palindromo(lista):
    for ind in range(len(lista)//2):
        if lista[ind] != lista[len(lista)-1-ind]:
            return "N"
    return "S"


# principal
entrada = input()
VOGAIS = "aeiou"
soVogais=""
for letra in entrada:
    if letra in VOGAIS:
        soVogais += letra
print(palindromo(soVogais))

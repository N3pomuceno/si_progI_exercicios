#Programa


#Subprogramas
def calculo(num1, num2, let):
    num1 = int(num1)
    num2 = int(num2)
    if num1 == num2:
        print(num1*num2)
    elif ord(let)>=ord("A") and ord(let)<=ord("Z"):
        print(num2-num1)
    elif ord(let)>=ord("a") and ord(let)<=ord("z"):
        print(num2+num1)
    return None

#principal
NUMDECARACTERES = 3
numDeCasos = int(input())
for ind in range(numDeCasos):
    caso = input()
    digitoUm = caso[0]
    digitoDois = caso[2]
    letra = caso[1]
    calculo(digitoUm, digitoDois, letra)


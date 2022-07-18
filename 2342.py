#programa

#Subprograma

#Principal
valorLimite = int(input())
num1, oper, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

#operação a ser feita
if oper == "+":
    operacao = num1+num2
elif oper == "*":
    operacao = num1*num2

#Verificação ser é overflow
if operacao > valorLimite:
    print("OVERFLOW")
else:
    print("OK")



#Programa
#Subprogramas
def mmc(dvd1, dvs1, dvd2, dvs2):
    if dvs1 == dvs2:
        multiplo = dvs1
    else:
        multiplo = dvs1*dvs2
        dvd1 = dvd1*dvs2
        dvd2 = dvd2*dvs1
        dvs1 = dvs2 = multiplo

    return dvd1, dvs1, dvd2, dvs2

def simplificacao(num1, num2):
    num = evidencia(num2, num1)
    print("{} {}".format(num1//num, num2//num))
    return None

def evidencia(n2, n1):
    evid = 1
    for num in range(2, n2+1):
        if n1 % num == 0 and n2 % num == 0:
            evid = num
    return evid

#Principal
dividendo1, divisor1, dividendo2, divisor2 = map(int, input().split())

dividendo1, divisor1, dividendo2, divisor2 = mmc(dividendo1, divisor1, dividendo2, divisor2)

resultado = dividendo1+dividendo2

simplificacao(resultado, divisor1)

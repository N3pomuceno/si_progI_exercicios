def LED(num):
    valores = [[1,2],[2,5],[3,5],[4,4],[5,5],[6,6],[7,3],[8,7],[9,6],[0,6]]
    numLED = 0
    for caracter in range(len(num)):
        for i in range(10):
            if int(num[caracter]) == valores[i][0]:
                numLED += valores[i][1]
    print("{} leds".format(numLED))
    return None

valor = int(input())
for i in range(valor):
    numero = input()
    LED(numero)
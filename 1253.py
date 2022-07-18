
def cripta(text, param):
    resultado = ""
    for c in range(len(text)):
        if ord(text[c]) - param < 65:
            newParam = 65 - ord(text[c]) + param
            resultado += chr(90 - newParam + 1)
        else:
            resultado += chr(ord(text[c]) - param)
    print(resultado)
    return None

valor = int(input())
for i in range(valor):
    texto = input()
    variacao = int(input())
    cripta(texto, variacao)
def maquina(falha, num):
    text = str(num)
    falhatext = str(falha)
    resposta = ""
    for caracter in range(len(text)):
        if text[caracter] != falhatext:
            resposta += text[caracter]
    if resposta == "":
        resposta = "0"
    num = int(resposta)
    mostrar(num)
    return None

def mostrar(resp):
    print("{:d}".format(resp))
    return None

d,n = map(int, input().split())
while d != 0 and n != 0:
    maquina(d,n)
    d,n = map(int, input().split())
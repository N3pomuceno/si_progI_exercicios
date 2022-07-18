def contrario(text):
    resultado = ""
    resultado2 = ""
    for letra in range(len(text)//2):
        resultado += text[len(text)//2 - 1 - letra]
        resultado2 += text[len(text) - 1 - letra]
    frase = resultado+resultado2
    print(frase)
    return None


valor = int(input())
for i in range(valor):
    texto = input()
    contrario(texto)
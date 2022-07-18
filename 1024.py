def trocar(pal):
    temp = ""
    ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxwyz"
    for pos in range(len(pal)):
        if pal[pos] in ALFABETO:
            temp += chr(ord(pal[pos])+3)
        else:
            temp += pal[pos]
    pal = temp
    temp2 = ""
    for pos in range(len(pal)):
        temp2 += temp[len(pal)-1-pos]
    pal = temp2
    temp3 = ""
    for pos in range(len(pal)):
        if pos < len(pal)//2:
            temp3 += temp2[pos]
        else:
            temp3 += chr(ord(temp2[pos])-1)
    pal = temp3
    print(pal)
    return None

valor = int(input())
palavra = input()
for i in range(valor):
    trocar(palavra)
    palavra = input()
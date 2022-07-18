#programa


#Subprogramas



#Principal
precoA, precoG, rendiA, rendiG = map(float, input().split())

#Preço por quilometro
pQA = precoA/rendiA
pQG = precoG/rendiG

#Comparação
if pQG <= pQA:
    print("G")
else:
    print("A")
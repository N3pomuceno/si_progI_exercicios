#Esse problema ficaria quilométrico se fosse uma lista imensa de produtos
#E só pode comprar um produto de cada vez, e não uma seleção deles

#Nesse códido não leva a possibilidade de escrever outro código além de 1 a 5
code, qtd = list(map(int,input().split()))
if code==1:
    tot = qtd * 4
    print("Total: R$ {:.2f}".format(tot))
elif code==2:
    tot = qtd * 4.5
    print("Total: R$ {:.2f}".format(tot))
elif code==3:
    tot = qtd * 5
    print("Total: R$ {:.2f}".format(tot))
elif code==4:
    tot = qtd * 2
    print("Total: R$ {:.2f}".format(tot))
else:
    tot = qtd * 1.5
    print("Total: R$ {:.2f}".format(tot))
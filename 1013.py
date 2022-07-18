valores = input().split()
e0 = int(valores[0])
e1 = int(valores[1])
e2 = int(valores[2])

m = ( e0 + e1 + abs(e0 - e1)) // 2
M = ( m + e2 + abs(m - e2)) // 2
#notar que é dividido por duas barras para sair um valor integer e não ter problema com o print
# para o format de integer d

#print("%d eh o maior"%(M))
print("{:d} eh o maior".format(M))

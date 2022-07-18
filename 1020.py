D = int(input())
A = D // 365
M = ( D % 365) // 30
R = ( D % 365) % 30

print("{} ano(s)".format(A))
print("{} mes(es)".format(M))
print("{} dia(s)".format(R))

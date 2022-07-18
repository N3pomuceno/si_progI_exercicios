a,b,c,d =list(map(int,input().split()))
afl = float(a)

if (b > c)and(d > a)and(c + d > a + b)and(c>0)and(d>0)and(a/2==afl/2):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")




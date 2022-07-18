val = float(input())
a = "[0,25]"
b = "(25,50]"
c = "(50,75]"
d = "(75,100]"
if 0 <= val <= 25:
    print("Intervalo {}".format(a))
elif 25 < val <= 50:
    print("Intervalo {}".format(b))
elif 50 < val <= 75:
    print("Intervalo {}".format(c))
elif 75 < val <= 100:
    print("Intervalo {}".format(d))
else:
    print("Fora de intervalo")

n = int(input())
cem = n // 100
cinq = (n % 100) // 50
vin = ((n % 100) % 50) // 20
dez = (((n % 100) % 50) % 20) // 10
cinc = ((((n % 100) % 50) % 20) % 10) // 5
dois = (((((n % 100) % 50) % 20) % 10) % 5) // 2
um = (((((n % 100) % 50) % 20) % 10) % 5) % 2

print(n)
print("{} nota(s) de R$ 100,00".format(cem))
print("{} nota(s) de R$ 50,00".format(cinq))
print("{} nota(s) de R$ 20,00".format(vin))
print("{} nota(s) de R$ 10,00".format(dez))
print("{} nota(s) de R$ 5,00".format(cinc))
print("{} nota(s) de R$ 2,00".format(dois))
print("{} nota(s) de R$ 1,00".format(um))

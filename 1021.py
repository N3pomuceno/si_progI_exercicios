nOrigin = float(input())
n = int(100 * nOrigin)
#Cédulas
cem = n // 10000
cinq = (n % 10000) // 5000
vin = ((n % 10000) % 5000) // 2000
dez = (((n % 10000) % 5000) % 2000) // 1000
cinc = ((((n % 10000) % 5000) % 2000) % 1000) // 500
dois = (((((n % 10000) % 5000) % 2000) % 1000) % 500) // 200
#Moedas
um = ((((((n % 10000) % 5000) % 2000) % 1000) % 500) % 200) // 100
cinqCent = ((((((((n % 10000) % 5000) % 2000) % 1000) % 500) % 200) % 100)// 50)
vinCent = ((((((((n % 10000) % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) // 25
dezCent = (((((((((n % 10000) % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) % 25) // 10
cincCent = ((((((((((n % 10000) % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) % 25) % 10) // 5
umCent = (((((((((((n % 10000) % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) % 25) % 10) % 5) % 5

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(cem))
print("{} nota(s) de R$ 50.00".format(cinq))
print("{} nota(s) de R$ 20.00".format(vin))
print("{} nota(s) de R$ 10.00".format(dez))
print("{} nota(s) de R$ 5.00".format(cinc))
print("{} nota(s) de R$ 2.00".format(dois))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(um))
print("{} moeda(s) de R$ 0.50".format(cinqCent))
print("{} moeda(s) de R$ 0.25".format(vinCent))
print("{} moeda(s) de R$ 0.10".format(dezCent))
print("{} moeda(s) de R$ 0.05".format(cincCent))
print("{} moeda(s) de R$ 0.01".format(umCent))

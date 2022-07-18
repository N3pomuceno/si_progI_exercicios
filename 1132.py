x = int(input())
y = int(input())
tot = 0
if x > y:
    d = y
    y = x
    x = d

for i in range (x,y+1):
    if i % 13 != 0:
        tot += i
print(tot)
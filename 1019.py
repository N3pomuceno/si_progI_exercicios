T = int(input())
hr = T // 3600
min = (T % 3600) // 60
sec = (T % 3600) % 60

print("{}:{}:{}".format(hr,min,sec))

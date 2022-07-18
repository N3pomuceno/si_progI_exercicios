# Programa

# Subprogramas
def local(vT, nums):
    total = 0
    for posicao in range(len(nums)):
        total += nums[posicao]
        if total == vT:
            return posicao

# Principal
num = int(input())
nums = list(map(int, input().split()))

# valor total para os dois distritos
valorTotal = 0
for numero in nums:
    valorTotal += numero
valorTotal //= 2

# achar a posição certa
pos = local(valorTotal, nums)
print(pos+1)

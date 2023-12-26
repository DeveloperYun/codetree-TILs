binary=list(map(int,list(input())))
num = 0

for i in range(5):
    num = num * 2 + binary[i]

print(num)
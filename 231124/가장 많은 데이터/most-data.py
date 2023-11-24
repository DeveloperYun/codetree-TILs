n=int(input())
d={}

for i in range(n):
    x=input()

    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

print(max(d.values()))
a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))

s1 = set(b)
s2 = set(d)

for elem in range(c):
    if d[elem] in s1:
        print(1)
    else:
        print(0)
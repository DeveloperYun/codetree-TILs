n,m=map(int,input().split())
s=list(map(int,input().split()))
d={}

for i in range(n):
    if s[i] not in d:
        d[s[i]] = 1
    
    else:
        d[s[i]] += 1

x=list(map(int,input().split()))
for i in range(m):
    if x[i] not in d:
        print("0",end=" ")
    else:
        print(d[x[i]],end=" ")
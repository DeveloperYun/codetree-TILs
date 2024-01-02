n,t=map(int,input().split())

first=list(map(int,input().split()))
second=list(map(int,input().split()))
s=first+second

while t>0:
    t -= 1

    temp = s[-1]
    for i in range(2*n-1,0,-1):
        s[i] = s[i-1]
    s[0] = temp

for i in range(2*n):
    if i==n:
        print()
    print(s[i],end=" ")
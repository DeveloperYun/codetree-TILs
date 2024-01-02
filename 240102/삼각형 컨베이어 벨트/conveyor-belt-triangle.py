n,t=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

s=a+b+c

while t>0:
    t -= 1

    temp = s[-1]
    for i in range(3*n-1,0,-1):
        s[i] = s[i-1]
    s[0] = temp

for i in range(3*n):
    if i%n==0 and i>0:
        print()
    print(s[i],end=" ")
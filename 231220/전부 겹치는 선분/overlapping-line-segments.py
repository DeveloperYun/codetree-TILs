import sys
n=int(input())
line=[]
for _ in range(n):
    x1,x2=map(int,input().split())
    line.append((x1,x2))

for i in range(1,101):
    cnt=0
    for x1,x2 in line:
        if x1<=i<=x2:
            cnt += 1
    
    if cnt == n:
        print("Yes")
        sys.exit(0)
print("No")
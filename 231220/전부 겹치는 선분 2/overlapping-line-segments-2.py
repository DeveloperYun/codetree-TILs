n = int(input())
check=[0] * 101
for _ in range(n):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        check[i] +=1
cnt = 0
for i in range(101):
    if check[i] == n - 1:
        cnt = cnt + 1

if cnt > 0:
    print('Yes')
else:
    print('No')
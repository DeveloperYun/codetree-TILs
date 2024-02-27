n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
import sys
limit = -1

for i in range(n):
    dp[i] = limit
dp[0] = 0

for i in range(1,n):
    for j in range(0,i):
        if dp[j] == limit:
            continue

        if j + a[j] >= i:
            dp[i] = max(dp[i], dp[j]+1)

ans=0
d=max(dp)
if ans > d:
    print(ans)
else:
    print(d)
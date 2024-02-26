import sys
INTMIN = -sys.maxsize

n=int(input())
num=list(map(int,input().split()))
dp=[0]*n

for i in range(1,n):
    dp[i] = INTMIN

for i in range(1,n):
    for j in range(i):
        if dp[j] == INTMIN:
            continue
        
        if j+num[j] >= i:
            dp[i] = max(dp[i], dp[j]+1)

answer=0
for i in range(n):
    answer = max(answer, dp[i])
print(answer)
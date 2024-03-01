import sys
INT_MAX = sys.maxsize

n,m=map(int,input().split())
arr=list(map(int,input().split()))

dp = [INT_MAX]*(m+1)
dp[0]=0

for i in range(n):
    for j in range(m,-1,-1):
        if j>=arr[i]:
            if dp[j-arr[i]] == INT_MAX:
                continue
            
            dp[j] = min(dp[j], dp[j-arr[i]]+1)
ans=dp[m]

if ans==INT_MAX:
    ans=-1

print(ans)
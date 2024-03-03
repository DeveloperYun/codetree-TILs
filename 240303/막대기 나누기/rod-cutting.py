n=int(input())
money=[0]+list(map(int,input().split()))

dp = [-1] * (n+1)
dp[0]=0 


for i in range(1,n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], money[j] + dp[i-j])

print(dp[n])
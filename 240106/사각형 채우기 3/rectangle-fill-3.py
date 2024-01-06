n=int(input())
dp=[0]*1001

dp[1] = 3
dp[2] = 7
dp[3] = 22

for i in range(4,n+1):
    dp[i] = 3*dp[i-1] + dp[i-2] - dp[i-3]
print(dp[n]%1000000007)
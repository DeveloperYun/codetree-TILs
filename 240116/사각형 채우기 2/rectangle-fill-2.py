MOD = 10007

n=int(input())
dp = [0]*11111
dp[0] = 1
dp[1] = 1
dp[2] = 3
dp[3] = 5
for i in range(3,n+1):
    dp[i] = (dp[i-1] + 2*dp[i-2])%MOD

print(dp[n])
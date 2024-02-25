n = int(input())

num = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def initial():
    #start initial
    dp[0][n-1] = num[0][n-1]

    #col
    for i in range(1,n):
        dp[i][-1] = dp[i-1][-1] + num[i][-1]

    #upper row
    for i in range(n-2,-1,-1):
        dp[0][i] = dp[0][i+1] + num[0][i]

initial()

for i in range(1,n):
    for j in range(n-2,-1,-1):
        dp[i][j] = min(dp[i-1][j], dp[i][j+1]) + num[i][j]

print(dp[n-1][0])
n=int(input())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)] for _ in range(n)
]

def initial():
    dp[0][0] = grid[0][0]

    #0열 초기화
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    #대각선 초기화
    for i in range(1,n):
        dp[i][i] = dp[i-1][i-1] + grid[i][i]

initial()

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(dp[n-1][n-1])
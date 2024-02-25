n=int(input())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

dp=[
    [0 for _ in range(n)] for _ in range(n)
]

def initial():
    dp[0][0] = grid[0][0]

    for row in range(1,n):
        dp[row][0] = max(dp[row-1][0], grid[row][0])
    
    for col in range(1,n):
        dp[0][col] = max(dp[0][col-1], grid[0][col])
        
initial()

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])

print(dp[n-1][n-1])
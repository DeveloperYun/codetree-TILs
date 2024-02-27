import sys
MIN_INT = -sys.maxsize

n,m=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

dp = [
    [MIN_INT for _ in range(m)]
    for _ in range(n)
]

dp[0][0]=1 #시작지점은 1

for i in range(1,n):
    for j in range(1,m):

        #점프하기 전의 위치
        if grid[0][0] >= grid[i][j]: #시작위치
            continue
        else:
            dp[i][j] = 2 #첫 점프

        #2번째 이후 점프
        for x in range(1,i):
            for y in range(1,j):

                if grid[i][j] > grid[x][y]:
                    dp[i][j] = max(dp[i][j], dp[x][y]+1)

max_value = 0
for i in range(n):
    for j in range(m):
        max_value = max(max_value, dp[i][j])
print(max_value)
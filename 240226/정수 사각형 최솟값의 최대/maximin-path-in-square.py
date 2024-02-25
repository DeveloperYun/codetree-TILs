n = int(input())
num = []
for _ in range(n):
    temp = list(map(int,input().split()))
    num.append(temp)

dp = [
    [0]*n for _ in range(n)
]

def initial():
    dp[0][0] = num[0][0]

    for i in range(1,n):
        #최좌측
        dp[i][0] = min(dp[i-1][0], num[i][0])

        #최상단
        dp[0][i] = min(dp[0][i-1],num[0][i])

initial()

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), num[i][j])
print(dp)

print(dp[n-1][n-1])
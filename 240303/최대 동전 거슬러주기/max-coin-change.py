n,m=map(int,input().split())
coins=list(map(int,input().split()))

'''
dp[i] : 금액 i를 거슬러줄때 최대 동전의 수



'''
dp = [-1]*(m+1) 
dp[0] = 0 

for i in range(1,m+1):
    for j in range(n):
        if i >= coins[j]: #합이 아직 코인보다 크다면
            if dp[i-coins[j]] == -1:
                continue

            dp[i] = max(dp[i], dp[i-coins[j]] + 1)

answer=dp[m]
if answer == -1:
    print(-1)
else:
    print(answer)
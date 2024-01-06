n = int(input())

def solution(n):
    dp = [0 for _ in range(n+1)] // 문제 발생 지점
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(0, i):
            dp[i] += dp[j] * dp[i-j-1]
    
    return dp[n]

print(solution(n))
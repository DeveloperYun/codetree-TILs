import sys


num = int(input())

a = [0] + list(map(int, input().split()))

dp = [0 for _ in range(num + 1)]


dp[1] = 1
for i in range(1, num+1):
    for j in range(i):
        if(a[j] < a[i]):
            dp[i] = max(dp[i], dp[j]+1) #이부분이 이해가 가질 않습니다.
print(max(dp))
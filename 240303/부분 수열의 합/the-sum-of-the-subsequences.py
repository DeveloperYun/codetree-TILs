n,m=map(int,input().split())
arr=list(map(int,input().split()))

'''
dp[i] = 합이 i가 되는데 가능한 최소 수열 길이
'''

dp=[99999]*(m+1)
dp[0]=0 

for i in range(n): #i번 원소를 사용

    for j in range(m,-1,-1): #합이 j인 경우 

        if j>=arr[i]:
            dp[j] = min(dp[j],dp[j-arr[i]]+1)

answer=dp[m]
if answer==99999:
    print("No")
else:
    print("Yes")
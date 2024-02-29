n=int(input())
alba=[]
for _ in range(n):
    start,end,price = map(int,input().split())
    alba.append((start,end,price))

dp=[0]*n
dp[0] = alba[0][2] 

for i in range(1, n):

    if alba[i][0] <= alba[i-1][1]: #겹친다 
        dp[i] = max(dp[i-1], alba[i][2])
    else:
        dp[i] = dp[i-1] + alba[i][2]

print(max(dp))
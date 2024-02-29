n=int(input())
alba=[]
for _ in range(n):
    start,end,price = map(int,input().split())
    alba.append((start,end,price))

dp=[0]*n
dp[0] = alba[0][2] 
#처음에 dp=[10,0,0] 으로 초기화 

for i in range(1, n): #i번째 알바 
    #alba[1] = (1,6,15)
    ends = alba[i][1] 
    i_start = alba[i][0] 

    for j in range(i): #0~i번째 dp 탐색
        
        if alba[j][1] >= i_start : #겹친다 
            dp[i] = max(alba[i][2], dp[i])

        else:
            dp[i] = max(dp[i],dp[j] + alba[i][2])

print(max(dp))
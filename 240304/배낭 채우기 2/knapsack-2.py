n,m=map(int,input().split())
weight=[0 for _ in range(n+1)]
value=[0 for _ in range(n+1)]

for i in range(1,n+1):
    weight[i],value[i] = map(int,input().split())


dp = [0 for _ in range(m+1)]
dp[0] = 0

for i in range(1,m+1): #무게의 합이 i 까지일 때
    for w,v in zip(weight,value):
        
        if i >= w:
            dp[i] = max(dp[i], dp[i-w]+v)

print(dp[-1])
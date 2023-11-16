import sys
n,h,t = map(int,input().split())
height = list(map(int,input().split()))
ans = sys.maxsize

#최소 2번이상 4높이로 나오게 
for i in range(n-t+1): 
    cnt = 0
    for j in range(i,i+t):
        cnt += abs(height[j]-h)
    ans = min(cnt,ans)

print(ans)
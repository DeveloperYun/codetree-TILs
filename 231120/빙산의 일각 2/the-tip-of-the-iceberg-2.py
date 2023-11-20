n=int(input())
h=[]
for i in range(n):
    x=int(input())
    h.append(x)

start=min(h)
end=max(h)
ans=0
for i in range(start,end):
    # i = 해수면의 높이
    cnt = 1
    for j in range(n-1):
        if h[j] - i > 0 and h[j+1]-i == 0:
            cnt += 1
    
    ans = max(ans,cnt)
print(ans)
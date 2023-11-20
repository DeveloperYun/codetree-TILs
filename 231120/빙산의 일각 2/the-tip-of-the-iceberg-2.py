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
    cnt = 0
    if h[0] > i:
        cnt += 1

    for j in range(1,n):
        if h[j] > i and h[j-1] <= i:
            cnt += 1
    
    ans = max(ans,cnt)
print(ans)
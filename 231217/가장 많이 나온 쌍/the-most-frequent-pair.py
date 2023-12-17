n,m=map(int,input().split())

segments=[]
for i in range(m):
    a,b=map(int,input().split())
    segments.append((a,b))

max_cnt=0
for x in range(1,101):
    overlap = 0
    for i in range(m):
        x1, x2 = segments[i]
        if x1 <= x and x <= x2:
            overlap += 1
    
    max_cnt = max(max_cnt,overlap)
print(max_cnt-1)
n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 0

segments.sort(lambda x:(x[0],x[1]))
start = segments[0][0]
end = segments[-1][1]

dp = [1]*n

def overlapped(seg1, seg2):
    (ax1, ax2), (bx1, bx2) = seg1, seg2

    # 두 선분이 겹치는지 여부는
    # 한 점이 다른 선분에 포함되는 경우로 판단 가능합니다. 
    return (ax1 <= bx1 and bx1 <= ax2) or (ax1 <= bx2 and bx2 <= ax2) or \
           (bx1 <= ax1 and ax1 <= bx2) or (bx1 <= ax2 and ax2 <= bx2)


for i in range(1,n):
    nowx,nowy = segments[i]
    
    for j in range(0,i):
        bx,by = segments[j]

        #겹친다면 continue
        if overlapped((nowx,nowy),(bx,by)):
            continue
        
        dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
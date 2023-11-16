import sys
n, h, t = tuple(map(int,input().split()))
arr = list(map(int,input().split()))

min_cnt = sys.maxsize
for i in range(n-t):
    cnt = 0
    for j in range(i,i+t):
        if arr[j] != h:
            cnt = cnt + abs(h-arr[j])
    min_cnt = min(min_cnt, cnt)
print(min_cnt)
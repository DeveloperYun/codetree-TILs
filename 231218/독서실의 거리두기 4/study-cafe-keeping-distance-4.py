n=int(input())
arr=list(input()) # 10001001000010


def min_dist():
    dist = n
    # 둘 다 1인 곳에 대해
    # 모든 쌍을 조사하여, 그 중 가장 가까운 거리를 구합니다.
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == '1' and arr[j] == '1':
                dist = min(dist, j - i)
    
    return dist

ans = 0
# 들어갈 두 군데를 일일히 지정해본다
for i in range(n):
    if arr[i] == '0':
        arr[i] = '1'

        for j in range(i+1,n):
            if arr[j] == '0':
                arr[j] = '1'

                ans = max(ans, min_dist())

                arr[j] = '0'
        arr[i] = '0'
    
print(ans)
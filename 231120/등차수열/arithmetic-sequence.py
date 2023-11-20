n = int(input())

arr = list(map(int, input().split()))

min_val = min(arr)#3
max_val = max(arr)#7
ans = 0

for k in range(min_val, max_val):
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == 2 * k:
                cnt = cnt + 1
    
    ans = max(ans, cnt)
print(ans)
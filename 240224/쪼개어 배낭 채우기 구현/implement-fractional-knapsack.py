n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    arr[i].append(arr[i][1]/arr[i][0])
arr.sort(key=lambda x:-x[2])
i = 0
a = 0
while m > 0 and i < n:
    if m >= arr[i][0]:
        m -= arr[i][0]
        a += arr[i][1]
        i += 1
    else:
        a += arr[i][2]*m
        m = 0
        i += 1

print("{:.3f}".format(a))
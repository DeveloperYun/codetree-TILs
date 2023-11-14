n=int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

count = 0

for i in range(n):
    for j in range(n-2):
        for k in range(i+1,n):
            for l in range(n-2):
                count = max(count, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[k][l] + arr[k][l+1] + arr[k][l+2])

print(count)
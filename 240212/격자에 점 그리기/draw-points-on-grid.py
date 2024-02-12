n,m=map(int,input().split())
arr=[
    [0]*n for _ in range(n)
]
for i in range(1,m+1):
    r,c=map(int,input().split())
    r-=1
    c-=1
    arr[r][c] = i

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()
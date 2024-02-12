n,m=map(int,input().split())

arr=[
    [0]*n for _ in range(n)
]

for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    arr[a][b] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()
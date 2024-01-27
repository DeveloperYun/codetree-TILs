a=[
    list(map(int,input().split()))
    for _ in range(4)
]

x=0
x+=(a[0][0]+a[1][0]+a[1][1]+sum(a[2])-a[2][3]+sum(a[3]))
print(x)
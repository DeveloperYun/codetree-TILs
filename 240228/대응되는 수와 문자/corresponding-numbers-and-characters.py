n,m=map(int,input().split())
arr={}
arr2={}
for i in range(1,n+1):
    x=input()
    arr[x] = i
    arr2[str(i)] = x

for _ in range(m):
    y=input()
    if y.isdigit():
        print(arr2[y])
    else:
        print(arr[y])
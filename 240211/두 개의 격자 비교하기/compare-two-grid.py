n,m=map(int,input().split())
arr1 = []
for i in range(n):
    t = list(map(int,input().split()))
    arr1.append(t)
arr2 = []
for i in range(n):
    t = list(map(int,input().split()))
    arr2.append(t)

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()
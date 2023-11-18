k,n=map(int,input().split())

arr=[]
for i in range(k):
    t=list(map(int,input().split()))
    arr.append(t)

cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            continue

        flag = True
        for x in range(k):
            ii,ij=0,0
            for y in range(n):
                if arr[x][y] == i:
                    ii=y

                if arr[x][y] == j:
                    ij=y
            if ii>ij:
                flag=False
        
        if flag:
            cnt+=1

print(cnt)
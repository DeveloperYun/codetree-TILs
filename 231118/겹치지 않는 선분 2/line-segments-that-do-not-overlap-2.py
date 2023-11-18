n=int(input())
arr=[]
for i in range(n):
    x1,x2=map(int,input().split()) #(X1,0)(x2,1)
    arr.append((x1,x2))

cnt=0

for i in range(n):
    for j in range(n):
        if i==j:
            continue

        a1,a2=arr[i] #3,9
        b1,b2=arr[j] #7,8

        if a1<b2 and a2>b1 and b2>a2:
            
            cnt += 1

print(cnt)
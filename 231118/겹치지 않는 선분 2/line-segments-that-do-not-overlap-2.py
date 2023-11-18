n=int(input())
arr=[]
for i in range(n):
    x1,x2=map(int,input().split()) #(X1,0)(x2,1)
    arr.append((x1,x2))

cnt=0

for i in range(n):
    overlap=False
    for j in range(n):
        if i==j:
            continue

        a1,a2=arr[i] #x[i][0],x[i][1]
        b1,b2=arr[j] #x[j][0],x[j][1]

        if (a1<=b1 and a2>=b2) or (a1>=b1 and b2>a2):
            overlap = True
            break
    if overlap == False:
        cnt += 1

print(cnt)
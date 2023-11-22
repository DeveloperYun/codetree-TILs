n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for _ in range(m):
    a1,a2=map(int,input().split())
    b.append([a1-1,a2-1])

for i in range(m):
    for j in b:
        a1 = j[0]
        a2 = j[1]
        #1,2
        temp = 0
        for k in range(a1,a2+1):    
            temp += a[k]
        
        print(temp)
    break
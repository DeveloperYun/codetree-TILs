arr=[]
for _ in range(3):
    a=list(map(int,input().rstrip()))
    arr.append(a)

for i in range(1,10):
    for j in range(1,10):
        
        for k in range(3):
            for a,b,c in arr[k]:
                # 1 2 4
                # 3 3 2
                # 5 6 1

                if i in a
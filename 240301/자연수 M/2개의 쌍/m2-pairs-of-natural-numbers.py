n=int(input())
data=[]
m=0
for _ in range(n):
    x,y=map(int,input().split())
    m+=x
    if x>1:
        for i in range(x):
            data.append(y)
    else:
        data.append(y)

data.sort()

print(data[m//2-1]+data[m//2])
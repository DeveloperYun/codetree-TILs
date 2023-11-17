n=int(input())
arr=[]
for i in range(n):
    x,y=map(int,input().split())
    arr.append((x,y))

#arr = [(2,4),(1,1),(5,2),(17,25)]
xlist=[]
ylist=[]
for x,y in arr:
    xlist.append(x)
    ylist.append(y)

answer=[]

for i in range(n):
    tmpx = list(xlist)
    tmpy = list(ylist)

    del tmpx[i]
    del tmpy[i]

    answer.append(((max(tmpx)-min(tmpx)) * (max(tmpy)-min(tmpy))))
print(min(answer))
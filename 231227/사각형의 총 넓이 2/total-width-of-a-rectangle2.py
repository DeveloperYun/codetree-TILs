OFFSET=100
MAX_=200

n=int(input())

re=[
    tuple(map(int,input().split()))
    for _ in range(n)
]


ch=[
    [0]*(MAX_+1)
    for i in range(MAX_+1)
]


for x1,y1,x2,y2 in re:
    x1,y1=x1+OFFSET,y1+OFFSET
    x2,y2=x2+OFFSET,y2+OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
           ch[x][y]=1


ar=0
for x in range(0,MAX_+1):
    for y in range(0,MAX_+1):
        if ch[x][y]==1:
            ar+=1

print(ar)
n,m=map(int,input().split())
grid=[
    list(map(int,input().split())) for _ in range(n)
]

answer=0

def find(x1,y1,x2,y2):

    cnt=0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if grid[i][j] > 0:
                cnt += 1
            else:
                return -1
    
    return cnt

#모든 꼭지점을 찾아서 검사해본다.
#(i,j) , (k,l)
for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                answer = max(answer, find(i,j,k,l))

if answer > 0:
    print(answer)
else:
    print(-1)
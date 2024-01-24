n,r,c=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

r-=1
c-=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

x=r
y=c
answer=[]
answer.append(grid[x][y])
def simul():
    global x, y
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #벗어나지 않는다면 위치 갱신.
        if in_range(nx,ny) and grid[nx][ny] > grid[x][y]:
            x = nx
            y = ny
            
            return True
    
    return False

while True:
    exist = simul() 
    
    if not exist:
        break
    
    answer.append(grid[x][y])

for i in answer:
    print(i,end=' ')
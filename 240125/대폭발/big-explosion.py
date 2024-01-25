n,m,r,c=map(int,input().split())

grid=[
    [0]*n for _ in range(n)
]
temp=[
    [0]*n for _ in range(n)
]
r-=1
c-=1

grid[r][c] = 1
temp[r][c] = 1
def in_range(x,y):
    return 0<=x<n and 0<=y<n

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def boom(x,y,dist):
    
    for i in range(4):
        nx = x + dx[i]*dist
        ny = y + dy[i]*dist

        if in_range(nx,ny) and temp[nx][ny]==0:
            temp[nx][ny] = 1

    # for i in range(n):
    #     for j in range(n):
    #         print(grid[i][j],end=" ")
    #     print()

for time in range(1,m+1): #m초 까지 폭발 
    dist = 2 ** (time-1)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                boom(i,j,dist)
                # print()
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]
            

answer=0
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            answer += 1

print(answer)
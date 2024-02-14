from collections import deque

n,k=map(int,input().split())

grid=[]
for _ in range(n):
    s=list(map(int,input().split()))
    grid.append(s)

visited=[
    [False for _ in range(n)] for _ in range(n)
]

answer = 0
q = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def cango(x,y):
    return in_range(x,y) and not grid[x][y] and not visited[x][y] 

def bfs():
    while q:
        x, y = q.popleft()

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if cango(nx,ny):
                q.append((nx,ny))
                visited[nx][ny] = True


for _ in range(k):
    r,c = map(int,input().split())
    r-=1
    c-=1

    q.append((r,c))
    visited[r][c] = True

bfs()

for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            answer += 1
print(answer)
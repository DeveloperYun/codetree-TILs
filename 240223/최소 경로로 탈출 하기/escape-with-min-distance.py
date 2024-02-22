from collections import deque

n,m=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

visited=[
    [False for _ in range(m)]
    for _ in range(n)
]

step = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

q = deque()

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def cango(x,y):
    if not in_range(x,y):
        return False
    
    if grid[x][y] == 0:
        return False
    
    if visited[x][y]:
        return False

    return True

def bfs():
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if cango(nx,ny):
                push(nx,ny,step[x][y]+1)

push(0,0,0)
bfs()

print(step[n-1][m-1])
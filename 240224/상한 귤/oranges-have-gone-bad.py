from collections import deque

n,k = map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

#상한귤=2, 귤=1, 벽=0
step = [
    [0 for _ in range(n)] for _ in range(n)
]

visited = [
    [False for _ in range(n)] for _ in range(n)
]

#2에서 동시에 BFS 돌리면 된다.
q=deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def cango(x,y):
    if not in_range(x,y):
        return False
    
    if grid[x][y] == 0:
        return False
    
    if visited[x][y]:
        return False
    
    return True

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def bfs():
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if cango(nx,ny):
                push(nx,ny,step[x][y] + 1)

#애초에 못 가는 곳은 -1로 표시하자.
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            step[i][j] = -1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            push(i,j,0) #상한 귤 시작.
            visited[i][j] = True
            step[i][j] = 0

bfs()

for i in range(n):
    for j in range(n):
        if not visited[i][j] and step[i][j]==0:
            step[i][j] = -2
for i in range(n):
    for j in range(n):
        print(step[i][j],end=' ')
    print()
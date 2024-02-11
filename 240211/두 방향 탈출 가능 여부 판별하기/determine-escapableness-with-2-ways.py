n,m=map(int,input().split())
grid=[
    list(map(int,input().split())) for _ in range(n)
]

visited = [
    [False]*m for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y] == True:
        return False

    if grid[x][y] == 0:
        return False

    return True

def dfs(x,y):
    dx = [0, 1]
    dy = [1, 0]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if can_go(nx,ny):
            visited[nx][ny] = True
            dfs(nx,ny)

visited[0][0]=True
dfs(0,0)


if visited[n-1][m-1]:
    print(1)
else:
    print(0)
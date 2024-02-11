n = int(input())
grid = [
    list(map(int,input().split())) for _ in range(n)
]

visited = [
    [False] * n for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n 

def cango(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y]:
        return False
    
    if grid[x][y] == 0:
        return False
    
    return True

peoples = []

def dfs(x,y):
    global cnt
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if cango(nx,ny): #갈 수 있으면 
            visited[nx][ny] = True
            cnt += 1
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if cango(i,j):
            visited[i][j] = True
            cnt = 1
            dfs(i,j)
    
            peoples.append(cnt)

print(len(peoples))
peoples.sort()
for i in peoples:
    print(i)
from collections import deque

n,k=map(int,input().split())
grid = [
    list(map(int,input().split())) for _ in range(n)
]
start_x,start_y = map(int,input().split())

visited = [
    [False for _ in range(n)] for _ in range(n)
]

q = deque()

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x,y,temp):
    if not in_range(x,y):
        return False

    if visited[x][y] or grid[x][y]>temp:
        return False

    return True


def bfs():
    while q:
        x,y = q.popleft()

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if can_go(nx,ny,grid[x][y]):
                q.append((nx,ny))
                visited[nx][ny] = True

def find_max():
    

for _ in range(k):
    #k번 반복할 때 마다 visited 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    q.append((start_x-1,start_y-1))
    visited[start_x-1][start_y-1] = True

    bfs()
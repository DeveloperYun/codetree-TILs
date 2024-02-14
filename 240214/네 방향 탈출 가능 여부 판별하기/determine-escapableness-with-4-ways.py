from collections import deque

n,m=map(int,input().split())
grid=[
    list(map(int,input().split())) for _ in range(n)
]

visited=[
    [False for _ in range(m)] for _ in range(n)
]


def in_range(x,y):
    return x>=0 and y>=0 and x<n and y<m

def cango(x,y):
    return in_range(x,y) and grid[x][y] and not visited[x][y]

q = deque()
def bfs():
    while q:
        x,y = q.popleft()

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if cango(nx,ny):
                q.append((nx,ny))
                visited[nx][ny] = True

q.append((0,0))
visited[0][0]=True

bfs()

# 우측 하단을 방문한 적이 있는지 여부를 출력합니다.
answer = 1 if visited[n - 1][m - 1] else 0
print(answer)
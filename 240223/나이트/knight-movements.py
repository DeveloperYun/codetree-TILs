from collections import deque

n=int(input())
r1,c1,r2,c2=map(int,input().split())

r1-=1
c1-=1
r2-=1
c2-=1

q=deque()
step = [
    [0 for _ in range(n)] for _ in range(n)
]
visited = [
    [False for _ in range(n)] for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def bfs():
    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [1,2,2,1,-1,-2,-2,-1]

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if in_range(nx,ny) and not visited[nx][ny]:
                push(nx,ny,step[x][y]+1)

push(r1,c1,0)
bfs()

if visited[r2][c2]==False:
    print(-1)
else:
    print(step[r2][c2])
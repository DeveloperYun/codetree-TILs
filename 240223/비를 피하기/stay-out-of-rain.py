from collections import deque

n,h,m = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

#0은 이동가능 / 1은 벽 / 2는 사람의 위치 / 3은 목적지
#각 사람의 위치에서 BFS를 시작해서, 가장 가까운 목적지까지 거리를 계산하면된다.
#만약 절대 비를 못 피한다면 -1을 출력한다.

step = [
    [0 for _ in range(n)] for _ in range(n)
]

visited = [
    [False for _ in range(n)] for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def cango(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y]:
        return False

    if grid[x][y] == 1:
        return False #벽이면 못감 (벽만 못감)

    return True

q = deque()

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def clear_visit_step():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

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

answer=[
    [0 for _ in range(n)] for _ in range(n)
]

#시작지점이 h 개
for i in range(n):
    for j in range(n):
        clear_visit_step()
        if grid[i][j] == 2:#사람의 현재 위치 
            push(i,j,0)
            bfs()
            temp = 9999999999
            for x in range(n):
                for y in range(n):
                    if grid[x][y]==3:
                        temp = min(temp, step[x][y])
            
            if temp == 0:
                answer[i][j]=-1
            else:   
                answer[i][j] = temp

for i in range(n):
    for j in range(n):
        print(answer[i][j],end=' ')
    print()
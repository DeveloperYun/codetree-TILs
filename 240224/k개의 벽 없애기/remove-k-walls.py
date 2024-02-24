from collections import deque
from itertools import combinations

n,k=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]
r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
r1,c1,r2,c2 = r1-1, c1-1, r2-1, c2-1

step=[
    [0 for _ in range(n)] for _ in range(n)
]

visited=[
    [False for _ in range(n)] for _ in range(n)
]

walls=[]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            walls.append((i,j))

# 벽=1 
# k개의 벽을 없앨 수 있다.
# k개를 없앤 뒤에 최소 도달 시간을 구해야한다.
q = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def clear_visited_step():
    for i in range(n):
        for j in range(n):
            step[i][j] = 0
            visited[i][j] = False

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def can_go(x,y):
    if not in_range(x,y): return False

    if visited[x][y]: return False

    if grid_copy[x][y] == 1: return False

    return True

def bfs():
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)

answer = 9999999999
#벽 중 k개를 0으로 바꿔주고, BFS 탐색을 진행한다.
trans = list(combinations(walls,k))

import copy
for t in trans:
    grid_copy = copy.deepcopy(grid)
    clear_visited_step() 
    for t2 in t:
        x,y = t2
        grid_copy[x][y] = 0 #벽을 부순다.
    
    #부쉈으니까 이제 bfs 하면된다.
    push(r1,c1,0)
    bfs()
 
    if visited[r2][c2]:
        answer = min(answer,step[r2][c2])

print(answer)
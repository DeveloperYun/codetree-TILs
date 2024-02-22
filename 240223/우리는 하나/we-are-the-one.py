from collections import deque
from itertools import combinations

n,k,u,d = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)] for _ in range(n)
]

'''
grid 에서 k개의 도시를 겹치지 않게 고른다.

고른 k개의 도시로부터 BFS 탐색을 실시하는데, 이 때 
인접한 도시와의 높이 차가 u이상 d이하여야만 이동 가능하다.
(자기자신 포함)
'''
answer = 0

#k개의 도시를 고른다.
coord=[]
for i in range(n):
    for j in range(n):
        coord.append((i,j))

cities = list(combinations(coord,k))

def visit_clear():
    global visited
    
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y,px,py):
    if not in_range(x,y):
        return False
    
    if visited[x][y]:
        return False
    
    if abs(grid[x][y]-grid[px][py]) < u or abs(grid[x][y]-grid[px][py]) > d:
        return False

    return True

#bfs탐색
def bfs():
    while q:
        x, y = q.popleft()

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if can_go(nx,ny,x,y):
                q.append((nx,ny))
                visited[nx][ny] = True

            

for city in cities:
    # ((1, 1), (2, 2))
    # 각 city 에서 bfs를 실시한다.
    visit_clear()
    q = deque()
    for c in city:
        # (1,1)
        q.append(c)
        x,y = c
        visited[x][y] = True
    
    bfs()
    cnt=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
    
    answer = max(answer, cnt)

print(answer)
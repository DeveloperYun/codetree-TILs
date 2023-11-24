from collections import deque
from itertools import combinations

n,k,m = map(int,input().split())
#k = 시작점의 개수, m = 치워야하는 돌의 개수

grid = [ 
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)] for _ in range(n)
]

start_pos = []
for _ in range(k):
    r,c = map(int,input().split())
    start_pos.append((r,c))

#완전탐색 x BFS
def initialized_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x,y):
    if not in_range(x,y): #범위 이탈
        return False
    
    #돌이거나 방문했다면
    if grid_case[x][y]==1:
        return False
    
    if visited[x][y]:
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

            if can_go(nx,ny):
                q.append((nx,ny))
                visited[nx][ny] = True

'''
visited 초기화는 언제 해줘야하지
치워야 하는 돌의 모든 경우의 수에 대해서 반복할 때 해줘야한다.
모든 경우의 수에 대한 grid부터 재설정 해야한다.
'''
def generate_grid_variations(grid, num_removed):
    variations = []

    # 1의 위치 찾기
    one_positions = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

    # 가능한 모든 1 제거 조합 생성
    for indices in combinations(one_positions, num_removed):
        new_grid = [row.copy() for row in grid]
        for index in indices:
            new_grid[index[0]][index[1]] = 0
        variations.append(new_grid)

    return variations

num_removed = m
grid_list = generate_grid_variations(grid, num_removed)

'''
이제 각 grid_case에 대해서 모든 시작점에서 bfs를 해주기만하면 된다.
'''
answer=0
q = deque()
for grid_case in grid_list:
    cnt = 0 #갈수있는 곳 카운팅
    
    initialized_visited() #visited 초기화

    for i in range(k):
        q.append((start_pos[i][0]-1,start_pos[i][1]-1))
        visited[start_pos[i][0]-1][start_pos[i][1]-1] = True
    
    bfs()

    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                cnt += 1

    answer = max(answer,cnt)

print(answer)
from collections import deque

n, h, m = map(int, input().split())     # n: 격자 크기, h: 사람 명수, m: 비를 피할 수 있는 공간
a = [list(map(int, input().split())) for _ in range(n)] # 0: 이동 가능, 1: 벽이어서 이동 x, 2: 사람, 3: 비를 피할 수 있는 공간
visited = [[False for _ in range(n)] for _ in range(n)] # 방문 여부
tmp = [[0 for _ in range(n)] for _ in range(n)]         # 중간 과정 담는 배열
dirs = ((1,0),(0,1),(-1,0),(0,-1))
result = [[0 for _ in range(n)] for _ in range(n)]  # 0: 사람이 있던 칸이 아닐 때, -1: 사람이 비를 피할 수 없을 때, 양수: 최소시간
q = deque()

def initialize():   # 방문 배열과 각 사용자 별 최소시간 초기화
    for x in range(n):
        for y in range(n):
            visited[x][y] = False
            tmp[x][y] = 0
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    return in_range(x,y) and (a[x][y] != 1) and not visited[x][y] 
def bfs():
    min_len = []
    while q:
        cur = q.popleft()
        for d in range(4):
            nx, ny = cur[0]+dirs[d][0], cur[1]+dirs[d][1]
            if can_go(nx,ny):
                tmp[nx][ny] = tmp[cur[0]][cur[1]] + 1
                visited[nx][ny] = True
                q.append((nx,ny))
                if a[nx][ny] == 3: min_len.append((tmp[nx][ny]))
    if min_len == []: return -1
    return min(min_len)

    

for i in range(n):
    for j in range(n):
        if a[i][j] == 2:    # 만약 사람이라면
            initialize()    # 먼저 초기화 진행
            visited[i][j] = True    # 방문했다 표기
            q.append((i,j))
            result[i][j] = bfs()

for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()
n,m,t=map(int,input().split())

grid = [
    [[] for _ in range(n)] for _ in range(n)
]

next_grid = [
    [[] for _ in range(n)] for _ in range(n)
]

# 입력으로 주어진 방향을 정의한 dx, dy에 맞도록
# 변환하는데 쓰이는 dict를 정의합니다.
mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

def in_range(x,y):
    return 0<=x<n and 0<=y<n


def next_pos(x,y,movedir):
    dx = [-1,0,0,1]
    dy = [0,1,-1,0]

    nx = x + dx[movedir]
    ny = y + dy[movedir]
    if not in_range(nx,ny): #벽에 부딪히면 방향전환
        movedir = 3 - movedir
    else:
        x = nx
        y = ny
    
    return (x,y,movedir)

def move_all():
    #움직인다.
    #현재 grid에섯 (무게, 번호, 방향) 순서대로 저장되어있다.
    for x in range(n):
        for y in range(n):
            for w, num, movedir in grid[x][y]:
                nx, ny, next_dir = next_pos(x,y,movedir)
                next_grid[nx][ny].append((w,num,next_dir))

def sum_marbles():
    #next_grid로 겹쳐진 부분이 있는지 확인해줄 수 있다.
    for i in range(n):
        for j in range(n):
            if len(next_grid[i][j]) > 1: #2개 이상 한 좌표에 있으면 겹쳐져있는 것이므로.
                #(무게, 번호, 방향)
                #무게는 합쳐지고, 방향은 가장 큰 번호가 가리키는 방향으로 간다. 
                next_grid[i][j].sort(key=lambda x:x[1], reverse=True)
                new_weight = 0
                for k in next_grid[i][j]:
                    w,_,_ = k
                    new_weight += int(w)
                new_num = next_grid[i][j][0][1]
                new_dir = next_grid[i][j][0][2]

                next_grid[i][j] = [(str(new_weight),new_num,new_dir)]
                
def simulate():
    #중복탐지용으로 사용할 next_Grid를 초기화한다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = []
    
    #모든 구슬을 움직인다. 
    move_all()

    #겹치는걸 파악하고 합체시켜준다.
    sum_marbles()


    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

for i in range(1,m+1):
    r,c,d,weight = tuple(input().split())
    r, c = int(r)-1, int(c)-1

    #무게, 번호, 방향 순서대로 유지 
    grid[r][c].append((weight,i,mapper[d]))

for _ in range(t):
    simulate()


ans = sum([
    len(grid[i][j]) for i in range(n) 
    for j in range(n)
])

maxweight = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != []:
            maxweight = max(maxweight, int(grid[i][j][0][0]))
print(ans,maxweight)
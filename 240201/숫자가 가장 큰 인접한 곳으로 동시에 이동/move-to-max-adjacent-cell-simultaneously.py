n,m,t=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

count = [
    [0]*n for _ in range(n)
]

next_count = [
    [0]*n for _ in range(n)
]


for _ in range(m):
    r,c = map(int,input().split())
    r-=1
    c-=1

    count[r][c] = 1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def get_next_pos(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] #상 하 좌 우 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if in_range(nx,ny):
            break
    
    return nx, ny

def move(x,y):
    nx, ny = get_next_pos(x,y)

    next_count[nx][ny] += 1

def move_all():
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i,j)
    
    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]

def remove_duplicate_marbles():
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0

def simulate():
    #구슬을 한꺼번에 이동시킨다
    move_all()

    #움직인 이후 충돌이 일어나는 구슬을 지워준다.
    remove_duplicate_marbles()

#t초 동안 시뮬레이션
for _ in range(t):
    simulate()

answer = 0
for i in range(n):
    for j in range(n):
        if count[i][j]==1:
            answer += 1

print(answer)
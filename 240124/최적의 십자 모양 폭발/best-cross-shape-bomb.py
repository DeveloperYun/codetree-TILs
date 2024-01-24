import copy

n=int(input())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

next_grid=[
    [0 for _ in range(n)]
    for _ in range(n)
]
#모든 위치에 대해서 폭발을 진행해보고 최대 쌍을 갱신하는 방법
answer=0
temp = copy.deepcopy(grid)
#bomb_range boom
def in_bomb_range(x,y,center_x,center_y,bomb_range):
    #행 or 열 일치 && 폭발 범위 내에 위치 
    return (x==center_x or y==center_y) and abs(x-center_x)+abs(y-center_y)<bomb_range 


def check_double():
    cnt = 0
    #가로로 스캔하면서 연속되는 쌍 확인
    for i in range(n):
        for j in range(1,n):
            if grid[i][j] == grid[i][j-1] and grid[i][j]!=0 and grid[i][j-1] != 0:
                cnt += 1
    #세로로 스캔하면서 연속되는 쌍 확인 
    for j in range(n):
        for i in range(1,n):
            if grid[i][j] == grid[i-1][j] and grid[i][j]!=0 and grid[i-1][j] != 0:
                cnt += 1
    return cnt


def bomb(center_x, center_y):
    bomb_range = grid[center_x][center_y]
    
    #put in 0 that boombed
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i,j,center_x,center_y,bomb_range):
                grid[i][j] = 0

    #폭탄이 터진 이후 중력이 작용한걸 next_grid에 저장함.
    for j in range(n):
        next_row = n-1
        #왼쪽 열 부터 채워나간다.
        for i in range(n-1,-1,-1):
            if grid[i][j] != 0:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1 

    #grid로 next_grid를 옮겨준다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


for i in range(n):
    for j in range(n):
        bomb(i,j) # (i,j) 폭발
        #grid에 대해서 check 
        answer = max(answer,check_double()) #최대 값을 찾고나서

        #한번 찾고나서는 원래대로 grid를 복구해야하므로 원상복구시킨다. 
        for k in range(n):
            for l in range(n):
                grid[k][l] = temp[k][l]
                next_grid[k][l] = 0
        
 

print(answer)
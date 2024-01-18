n,m=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]
columns = []
for _ in range(m):
    x=int(input())
    columns.append(x)

def in_bomb_range(x,y,center_x,center_y,bomb_range):
    #같은 행 혹은 같은 열에 속해있어야하고 and 폭탄범위 안에있어야한다.
    if (x==center_x or y==center_y) and abs(x-center_x) + abs(y-center_y) < bomb_range:
        return True

    return False

def bomb(center_x,center_y):
    bomb_range = grid[center_x][center_y]

    #폭탄이 터질 위치를 0으로 채운다.
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i,j,center_x,center_y,bomb_range):
                grid[i][j]=0

    #폭탄이 터진 이후의 결과를 temp에 저장 (중력 적용)
    #열을 기준으로 shift 해준다고 생각한다. 
    for j in range(n):
        #각 열별로, 끝 행에서부터 첫 행까지 탐색하기 위한 것.
        next_row = n-1
        for i in range(n-1,-1,-1):#3,2,1,0
            if grid[i][j]!=0:
                #열 별로 진행하니까 열을 의미하는 j는 고정. 
                #변하는건 오직 행(next_row)이다. 
                next_grid[next_row][j] = grid[i][j]
                next_row-=1


for i in range(len(columns)):
    col = columns[i]
    col -= 1 #열
    for j in range(n): #행
        if grid[j][col]==0:
            continue
        else:
            bomb(j,col)
            break

temp = [[0]*n for _ in range(n)]
for j in range(n):
    t_row=n-1
    for i in range(n-1,-1,-1):
        if grid[i][j] != 0:
            temp[t_row][j] = grid[i][j]
            t_row -= 1

for i in range(n):
    for j in range(n):
        print(temp[i][j], end=" ")
    print()
print()
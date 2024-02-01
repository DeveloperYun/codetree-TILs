import copy

n,m,r,c=map(int,input().split())
go = list(map(str,input().split()))
r-=1
c-=1

grid=[
    [0]*n for _ in range(n)
]

#초기 주사위 상태 
dice = [
    [0,5,0],
    [4,6,3],
    [0,2,0]
]


def in_range(x,y):
    return 0<=x<n and 0<=y<n 

# 주사위를 굴렸을 때 주사위의 상태. 
def roll_dice(direction):
    global dice
    temp_dice = copy.deepcopy(dice) #dice 복사

    if direction == "L":
        temp_dice[1][0] = abs(7-dice[1][1])
        temp_dice[1][1] = dice[1][0]
        temp_dice[1][2] = dice[1][1]
    elif direction == "R":
        temp_dice[1][0] = dice[1][1]
        temp_dice[1][1] = dice[1][2]
        temp_dice[1][2] = abs(7-dice[1][1])
    elif direction == "D":
        temp_dice[0][1] = dice[1][1]
        temp_dice[1][1] = dice[2][1]
        temp_dice[2][1] = abs(7-dice[1][1])
    elif direction == "U":
        temp_dice[0][1] = abs(7-dice[1][1])
        temp_dice[1][1] = dice[0][1]
        temp_dice[2][1] = dice[1][1]

    #복사된 dice를 원본 dice에 적용
    for i in range(3):
        for j in range(3):
            dice[i][j] = temp_dice[i][j]

#초기 주사위 위치(r,c)
grid[r][c] = 6 #처음에는 시작좌표에 6이 있다

# 주사위를 m번 굴린다
for i in range(m):
    # 주사위를 굴리기 전에, 격자 밖으로 벗어나는지를 확인해야한다. 
    if go[i] == "L":
        if in_range(r,c-1):
            roll_dice("L")
            c-=1
            grid[r][c] = dice[1][1]
    elif go[i] == "R":
        if in_range(r,c+1):
            roll_dice("R")
            c+=1
            grid[r][c] = dice[1][1]
    elif go[i] == "D":
        if in_range(r+1,c):
            roll_dice("D")
            r+=1
            grid[r][c] = dice[1][1]
    else:
        if in_range(r-1,c):
            roll_dice("U")
            r-=1
            grid[r][c] = dice[1][1]


answer=0
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            answer += grid[i][j]
print(answer)
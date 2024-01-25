n=int(input())
x,y=map(int,input().split())
grid=[
    list(map(str,input().rstrip()))
    for _ in range(n)
]

x-=1
y-=1

# 동, 남, 서, 북 순으로 dx, dy를 정의합니다.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
startx,starty=x,y

answer=0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

#바라보는 방향을 어떻게 처리할 지 고민중. 
def solution():
    global x,y,answer,startx,starty
    curr_dir = 0 #시작할 때 동쪽을 바라보고 있으므로.
    exit = False

    while not exit: 
        
        nx = x + dx[curr_dir]
        ny = y + dy[curr_dir]

        if startx==x and starty==y and exit==False:
            answer = -1
            break
        # 바라보고 있는 방향으로 이동하는 것이 가능한 경우
        if in_range(nx,ny) == False: #격자 밖이라면
            answer += 1
            exit = True
        else:
            # 바라보고 있는 방향으로 이동하는 것이 가능하지 않은 경우
            if grid[nx][ny] == '#' :
                curr_dir = (curr_dir - 1 + 4)%4 #반시계 90도 회전            
            # 만약 그 방향으로 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 짚을 벽이 있다면
            elif in_range(nx+1,ny) and grid[nx+1][ny] == "#":
                x,y=nx,ny
                answer += 1
            # 만약 그 방향으로 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 벽이 존재하지 않는다면,
            else:
                x,y=nx,ny #현재 방향으로 한 칸 이동 후
                curr_dir = (curr_dir + 1) % 4 #시계방향 90도 회전 
                x,y=x+dx[curr_dir],y+dy[curr_dir] #진행 
                answer += 2

solution()
print(answer)
n,m=map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]


def in_range(x,y):
    return 0<=x<n and 0<=y<n

def swapping():
   
    
    #북쪽부터 시계방향
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]

    for k in range(1,n*n+1): #1부터 탐색
        x, y = 0, 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == k:
                    x = i
                    y = j
                    break

        #숫자의 좌표를 찾았다.
        #이제 해당 좌표 (x,y) 에서 8방 탐색을 해야한다.
        temp = []
        maxval=0
        maxx,maxy=0,0
        for i in range(8):#8방 탐색 시작
            nx = x + dx[i]
            ny = y + dy[i]

            #격자를 벗어나지 않고, 좌표값보다 큰 값이 8방탐색 중에 발견된다면 
            
            if in_range(nx,ny):
                if grid[nx][ny] > maxval:
                    maxval = grid[nx][ny]
                    maxx=nx
                    maxy=ny

        new_x = maxx
        new_y = maxy

        a=grid[x][y]
        grid[x][y] = grid[new_x][new_y]
        grid[new_x][new_y]=a
        

for i in range(m): #m번 반복
    swapping()

for i in range(n):
    for j in range(n):
        print(grid[i][j],end=" ")
    print()
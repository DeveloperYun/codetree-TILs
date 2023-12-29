n=int(input())
arr = [
    [0] * n for _ in range(n)
]

#역순으로 채워나가도 된다
def in_range(x,y):
    return 0<=x<n and 0<=y<n

dx = [0,1,0,-1]
dy = [1,0,-1,0]

x,y=n-1,n-1 #오른쪽 끝에서부터 시작한다.
dir_num = 2 #서쪽을 바라보고 있다

arr[x][y] = n*n

for i in range(n*n-1,0,-1): #24부터해서 1까지 
    while True:
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]

        if in_range(nx,ny) and arr[nx][ny] == 0:
            x,y=nx,ny
            arr[x][y] = i
            break
        else:
            #시계방향
            dir_num = (dir_num+1)%4

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
n,m=map(int,input().split())
board = []
for _ in range(n):
    temp = list(map(str,input().rstrip()))
    board.append(temp)

count = 0

#북,북동,동,남동,남,남서,서,북서
dx = [-1, -1, 0, 1, 1,  1,  0, -1]
dy = [ 0,  1, 1, 1, 0, -1, -1, -1]

def in_range(x,y):
    return x>=0 and y>=0 and x<n and y<m

for i in range(n):
    for j in range(m):
        if board[i][j] == "L":

            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]

                #방향은 여기서 고정된 상태.
                if 0<=nx<n and 0<=ny<m and board[nx][ny] == "E":
                    nnx = nx + dx[k]
                    nny = ny + dy[k]

                    if 0<=nnx<n and 0<=nny<m and board[nnx][nny] == "E":
                        count += 1
print(count)
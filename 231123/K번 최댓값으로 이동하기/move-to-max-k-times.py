from collections import deque
#변수입력----------------------------------------------------------#
N, K = tuple(map(int, input().split()))
graph=[]
for _ in range(N):
    graph.append(list(map(int, input().split())))
r,c=map(int,input().split())
#초기상태----------------------------------------------------------#
NO_EXIST=(-1,-1)
curr_cell=(r-1,c-1)
dx,dy=[0,-1,0,1],[-1,0,1,0]#좌상우하
visited=[[False for _ in range(N)]for _ in range(N)]
#함수선언----------------------------------------------------------#
def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<N
def can_go(x,y,max_n):
    return in_range(x,y) and graph[x][y]<max_n and not visited[x][y]
def reset_visited():
    for i in range(N):
        for j in range(N):
            visited[i][j]=False
def bfs():
    q=deque()
    x,y=curr_cell
    max_num = graph[x][y]
    q.append((x,y))
    visited[x][y]=True
    while q:
        rx,ry=q.popleft()
        for i in range(4):
            nx,ny=rx+dx[i],ry+dy[i]
            if can_go(nx,ny,max_num):
                q.append((nx,ny))
                visited[nx][ny]=True
def need_update(best_pos,new_pos):
    if best_pos==NO_EXIST:#딱 왔는데 초기값이면 그 위치로 갱신해야되니까
        return True
    best_x,best_y=best_pos
    new_x,new_y=new_pos
    return(graph[best_x][best_y], -best_x, -best_y)<(graph[new_x][new_y], -new_x, -new_y)

def move():
    global curr_cell
    reset_visited()
    bfs()#bfs를 통해 현재 cell과 max_n으로부터 이동 가능한 모든 영역의 방문표시
    best_pos=NO_EXIST
    for i in range(N):
        for j in range(N):
            if not visited[i][j] or (i,j)==curr_cell:
                #여기서 왜 NOT VISITED인지...?방문한 적이 있으면 건너뛰어야 하는거 아닐까
                #아..방문한 적 없다는건 갈 수 없는 영역이라는거니까 당연히 넘겨야되는거구나
                continue
            new_pos=(i,j)
            if need_update(best_pos,new_pos):
                best_pos=new_pos
    if best_pos==NO_EXIST:
        return False
    else:
        curr_cell=best_pos
        return True

for _ in range(K):
    is_move=move()
    if not is_move:
        break
final_x,final_y=curr_cell
print(final_x+1,final_y+1)
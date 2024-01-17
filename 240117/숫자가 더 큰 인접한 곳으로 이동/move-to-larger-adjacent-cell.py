n,r,c=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 1<=x<n and 1<=y<n
curr_x, curr_y = r-1,c-1
answer=[]
answer.append(grid[curr_x][curr_y])

#시작좌표에서 사방탐색을 진행한다.
def simulation():
    global curr_x,curr_y
    max_num=0
    max_pos = (-1,-1)

    dxs=[-1,1,0,0]
    dys=[0,0,-1,1]  

    while True:
        #curr_x,curr_y 좌표에서 사방 탐색을 진행한다. 
        for dx,dy in zip(dxs,dys):
            next_x, next_y = curr_x + dx, curr_y + dy

            if in_range(next_x,next_y) and grid[next_x][next_y]>max_num:
                max_num = grid[next_x][next_y]
                answer.append(max_num)
                curr_x,curr_y=next_x,next_y
                is_done = False
                break
        if is_done:
            break
        is_done = True

simulation()
for i in answer:
    print(i,end=" ")
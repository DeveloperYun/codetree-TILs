n,t=map(int,input().split())
command = list(input())
arr=[
    list(map(int,input().split())) for _ in range(n)
]

x,y=n//2,n//2 #시작 좌표

dx=[0,1,0,-1]
dy=[1,0,-1,0]

answer=arr[x][y]
curr_dir=3

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for i in range(len(command)):
    c_dir = command[i]

    if c_dir=="L":
        curr_dir = (curr_dir-1+4)%4
    elif c_dir=="R":
        curr_dir = (curr_dir + 1)%4
    else:
        x,y = x+dx[curr_dir],y+dy[curr_dir]

        if in_range(x,y) == False:
            x,y = x-dx[curr_dir],y-dy[curr_dir]
        else:
            answer += arr[x][y]

print(answer)
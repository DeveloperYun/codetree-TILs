n=int(input())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

answer=0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

#동 서 남 북
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def turn_dir(direct):
    pass

#동쪽으로 출발하는 왼쪽 모서리의 경우
for i in range(n):
    #출발좌표 = (i,0)
    x = i
    y = 0
    
    temp = 1
    dirction = 0 #처음에 동쪽
    while in_range(x,y):
        
        if grid[x][y] == 1:
            if dirction == 0:
                dirction = 3
            elif dirction == 3:
                dirction = 0
            elif dirction == 2:
                dirction = 1
            else:
                dirction = 2
        elif grid[x][y] == 2:
            if dirction == 0:
                dirction = 2
            elif dirction == 2:
                dirction = 0
            elif dirction == 1:
                dirction = 3
            else:
                dirction = 1

        x = x + dx[dirction]
        y = y + dy[dirction]
        temp += 1
      
    answer = max(answer,temp)  

#동쪽으로 출발하는 왼쪽 모서리의 경우
for i in range(n):
    #출발좌표 = (0,4),(1,4)
    x = i
    y = n-1
    
    temp = 1
    dirction = 1 #처음에 서쪽
    while in_range(x,y):
        
        if grid[x][y] == 1:
            if dirction == 0:
                dirction = 3
            elif dirction == 3:
                dirction = 0
            elif dirction == 2:
                dirction = 1
            else:
                dirction = 2
        elif grid[x][y] == 2:
            if dirction == 0:
                dirction = 2
            elif dirction == 2:
                dirction = 0
            elif dirction == 1:
                dirction = 3
            else:
                dirction = 1

        x = x + dx[dirction]
        y = y + dy[dirction]
        temp += 1
        
    answer = max(answer,temp)  

#남쪽으로 출발하는 왼쪽 모서리의 경우
for i in range(n):
    #출발좌표 = (4,0),(4,1)...
    x = n-1
    y = i
    
    temp = 1
    dirction = 2 #처음에 동쪽
    while in_range(x,y):
        
        if grid[x][y] == 1:
            if dirction == 0:
                dirction = 3
            elif dirction == 3:
                dirction = 0
            elif dirction == 2:
                dirction = 1
            else:
                dirction = 2
        elif grid[x][y] == 2:
            if dirction == 0:
                dirction = 2
            elif dirction == 2:
                dirction = 0
            elif dirction == 1:
                dirction = 3
            else:
                dirction = 1

        x = x + dx[dirction]
        y = y + dy[dirction]
        temp += 1
       
    answer = max(answer,temp)  

#북쪽으로 출발하는 왼쪽 모서리의 경우
for i in range(n):
    #출발좌표 = (0,0)(0,1)..
    x = 0
    y = i
    
    temp = 1
    dirction = 3 #처음에 동쪽
    while in_range(x,y):
        
        if grid[x][y] == 1:
            if dirction == 0:
                dirction = 3
            elif dirction == 3:
                dirction = 0
            elif dirction == 2:
                dirction = 1
            else:
                dirction = 2
        elif grid[x][y] == 2:
            if dirction == 0:
                dirction = 2
            elif dirction == 2:
                dirction = 0
            elif dirction == 1:
                dirction = 3
            else:
                dirction = 1

        x = x + dx[dirction]
        y = y + dy[dirction]
        temp += 1
       
    answer = max(answer,temp)  

print(answer)
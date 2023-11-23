n=int(input())
grid = [
    list(map(int,input().split())) for _ in range(n)
]

visited = [
    [False for _ in range(n)] for _ in range(n)
]

people_num = 0
people_nums = list()

def in_range(x,y):
    return x>=0 and y>=0 and x<n and y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y] or grid[x][y]==0:
        return False
    
    return True

def dfs(x,y):
    global people_num

    dx = [0,1,-1,0]
    dy = [-1,0,0,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if can_go(nx,ny):
            visited[nx][ny] = True

            people_num += 1
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = True
            people_num = 1

            dfs(i,j)

            people_nums.append(people_num)

# 각 마을 내 사람의 수를 오름차순으로 정렬합니다.
people_nums.sort()

print(len(people_nums))

for i in range(len(people_nums)):
    print(people_nums[i])
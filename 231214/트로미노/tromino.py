n,m=map(int,input().split())

grid=[]
for _ in range(n):
    t = list(map(int,input().split()))
    grid.append(t)

block = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]

def in_range(x,y,z): 
    for i in range(3):
        for j in range(3):
            if block[z][i][j] == 1:
                if x+i >= n or y+j >= m:
                    return False
    return True
    
def counst(x,y,z):
    cnt=0

    for i in range(3):
        for j in range(3):
            if block[z][i][j] == 1:
                cnt += grid[x+i][y+j]
    return cnt

maxnum=-1
for i in range(n):
    for j in range(m):
        for k in range(6):
            if in_range(i,j,k):
                blocknum = counst(i,j,k)
                maxnum = max(maxnum,blocknum)

print(maxnum)











'''
# ㄴ block test
# 경우의 수 4가지
def nieun_test(grid):
    pass

# ㅡ block test
def eu_test1(grid):
    def get_num(row, cs, ce):
        num = 0
        for col in range(cs,ce+1):
            num += grid[row][col]
        return num

    temp = 0
    for row in range(n):
        for col in range(m):
            if col + 2 >= m:
                continue
            
            num = get_num(row,col,col+2)
            temp = max(temp,num)    
    
    return temp

# l block test
def eu_test1(grid):
    def get_num(row, cs, ce):
        num = 0
        for col in range(cs,ce+1):
            num += grid[row][col]
        return num

    temp = 0
    for row in range(n):
        for col in range(m):
            if col + 2 >= m:
                continue
            
            num = get_num(row,col,col+2)
            temp = max(temp,num)    
    
    return temp
'''
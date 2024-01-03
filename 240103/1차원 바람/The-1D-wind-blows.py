n,m,q=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

#wind_info = (행, 바람의 방향)
'''
일단 전파된거 보기 전에 바람이 불어온대로 shift 한다.
'''

def shift(row,direction):
    #grid의 row-1 행을 dir 방향으로 shift
    if direction == "L":
        #오른쪽으로 shift 해야하므로 temp에는 끝을.
        temp = grid[row][-1]
        for i in range(m-1,0,-1):
            grid[row][i] = grid[row][i-1]

        grid[row][0] = temp  
    else:
        #왼쪽으로 shift 해야하므로 temp에는 앞을.
        temp = grid[row][0]
        for i in range(m-1):
            grid[row][i] = grid[row][i+1]

        grid[row][-1] = temp

def can_go(a,b):

    #rows 행을 기준으로 전파가 가능한지 파악
    for i in range(m):
        if a[i] == b[i]:
            return True
    
    return False

for _ in range(q):
    r,d=map(str,input().split())
    r=int(r)
    shift(r-1,d) #한 바람이 불었다.

    #이 아래로는 바람의 전파가 이어진다.
    memory = d
    #r의 위 아래로 분할 탐색
    rows = r-1 #rows=2

    #위로 전파 가능한지 판단
    for i in range(rows,0,-1):
        if can_go(grid[i],grid[i-1]):
            if d=='R':
                shift(i-1,'L')
                d='L'
            else:
                shift(i-1,'R')
                d='R'
        else:
            break
    d = memory
    #아래로 전파 가능한지 판단 
    for i in range(rows,n-1):
        if can_go(grid[i],grid[i+1]):
            if d=='R':
                shift(i+1,'L')
                d='L'
            else:
                shift(i+1,'R')
                d='R'

        else:
            break

for i in range(n):
    for j in range(m):
        print(grid[i][j],end=" ")
    print()
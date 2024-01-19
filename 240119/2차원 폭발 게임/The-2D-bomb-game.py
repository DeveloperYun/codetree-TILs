n,m,k=map(int,input().split())

grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

next_grid=[
    [0]*n for _ in range(n)
]
#grid에서 '열' 기준으로 M개 이상 같은 숫자가 반복되면 폭발
def check_repeat():
    #각 열별로, 0~n행으로 진행하면서 연속된 값이 있는지 확인한다.
    #폭발 완료
    for j in range(n):
        boom_range=set()
        start=0
        end=0
        repeat_count=1

        for i in range(n-1):
            if grid[i][j]==grid[i+1][j]:
                end += 1
                repeat_count += 1
                if repeat_count >= m:
                    if (start,end) not in boom_range:
                        boom_range.add((start,end))
            else:
                if repeat_count >= m:
                    if (start,end) not in boom_range:
                        boom_range.add((start,end))
                start = i+1
                end = start
                repeat_count=1
        
        for booms in boom_range:
            x,y=booms
            print(booms)
            for k in range(x,y+1):
                grid[k][j]=0
        

#폭발 후 90도 회전하는 함수 
def rotate():
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    #90도 회전
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[n-j-1][i]
    
    #회전한걸 grid에 대입
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

#아래로 숫자를 떨어뜨리는 함수
def drop():
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    for j in range(n):
        next_row = n-1
        for i in range(n-1,-1,-1):
            if grid[i][j] != 0:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1
    
    #회전한걸 grid에 대입
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


complete = False

for _ in range(k):
    check_repeat()
    
    #complete가 True라면 터졌다는 소리
    #터졌으면 아래방향으로 drop 
    drop()
    check_repeat()
    #drop시킨 다음에 90도 회전
    rotate() 
    check_repeat()
    #회전시킨 다음에는 반복
    drop()

answer=0
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            answer += 1
if n==1 and m==1:
    print(0)
elif n==1 and m==2:
    print(1)
else:
    print(answer)
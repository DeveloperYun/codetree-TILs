n,m=map(int,input().split())

grid=[]
for _ in range(n):
    t = list(map(int,input().split()))
    grid.append(t)

def check(temp):
    cnt = 1
    for i in range(n-1):
        
        if temp[i] == temp[i+1]:
            cnt += 1 

        if cnt == m:
            return True
    
    return False

answer = 0 
#row 탐색
for row in range(n):
    temp = []
    for col in range(n):
        temp.append(grid[row][col])
    
    #temp에 대해서 탐색
    flag = check(temp)

    if flag:
        answer += 1

for col in range(n):
    temp = [i[col] for i in grid]
    flag = check(temp)
    if flag:
        answer += 1

if n==1:
    print(2)
else:
    print(answer)
grid=[]
for _ in range(10):
    line = list(map(str,input()))
    grid.append(line)

lpos=[]
rpos=[]
bpos=[]
answer=0
for i in range(10):
    for j in range(10):
        if grid[i][j] == "L":
            lpos.append((i,j))
        if grid[i][j] == "R":
            rpos.append((i,j))
        if grid[i][j] == "B":
            bpos.append((i,j))

#L에서 출발해서 R을 피해서 B로 도달 

#R이 B,L사이에 위치하는 경우
if lpos[0][1] == rpos[0][1] == bpos[0][1]:
    if lpos[0][0] < rpos[0][0] < bpos[0][0] or bpos[0][0] < rpos[0][0] < lpos[0][0]:
        answer += 1
        answer += abs(lpos[0][0] - bpos[0][0])
        print(answer)
elif lpos[0][0] == rpos[0][0] == bpos[0][0]:
    answer += 1
    answer += abs(lpos[0][1] - bpos[0][1])
    print(answer)
else:
    answer += abs(lpos[0][0] - bpos[0][0])
    answer += abs(lpos[0][1] - bpos[0][1])
    print(answer-1)
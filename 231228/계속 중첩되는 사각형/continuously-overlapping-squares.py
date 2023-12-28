n=int(input())
rects = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

offset = 100
max_r = 200

checked = [
    [0]*(max_r+1) for _ in range(max_r+1)
]
#red = 1, blue = 2
cnt = 0
for x1,y1,x2,y2 in rects:
    cnt += 1
    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    if cnt%2 != 0: #홀수라면 레드
        for i in range(x1,x2):
            for j in range(y1,y2):
                checked[i][j] = 1
    else:
        for i in range(x1,x2):
            for j in range(y1,y2):
                checked[i][j] = 2

answer=0
for i in range(max_r+1):
    for j in range(max_r+1):
        if checked[i][j] == 2:
            answer += 1
print(answer)
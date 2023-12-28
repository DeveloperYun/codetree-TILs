rects = [
    tuple(map(int,input().split())) 
    for _ in range(3)
]

MAX_R = 2000
OFFSET = 1000

checked = [
    [0] * (MAX_R + 1) for _ in range(MAX_R+1)
]

minus=0
cnt=0
for x1,y1,x2,y2 in rects:
    cnt += 1
    x1,y1 = x1+OFFSET, y1+OFFSET
    x2,y2 = x2+OFFSET, y2+OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y] = 1

    if cnt==3:
        minus = (x2-x1) * (y2-y1)

area = 0
for x in range(MAX_R+1):
    for y in range(MAX_R+1):
        if checked[x][y] == 1:
            area += 1

print(area-minus)
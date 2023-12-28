rects = [
    tuple(map(int,input().split())) 
    for _ in range(3)
]

MAX_R = 2000
OFFSET = 1000

checked = [
    [0] * (MAX_R + 1) for _ in range(MAX_R+1)
]

row_min,row_max,col_min,col_max=9999,-9999,9999,-9999

for x1,y1,x2,y2 in rects:
    x1,y1 = x1+OFFSET, y1+OFFSET
    x2,y2 = x2+OFFSET, y2+OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y] = 1

            row_max = max([row_max,x1,x2])
            row_min = min([row_min,x1,x2])
            col_max = max([col_max,y1,y2])
            col_min = min([col_min,y1,y2])

area = 0
for x in range(0, MAX_R + 1):
    for y in range(0, MAX_R + 1):
        if checked[x][y]:
            area += 1

all_area = (row_max-row_min)*(col_max-col_min)
print(all_area-area+1)
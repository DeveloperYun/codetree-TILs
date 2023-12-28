n=int(input())
max_r = 200
offset = 100

rects = []
for _ in range(n):
    x1,y1=map(int,input().split())

    rects.append((x1,y1,x1+8,y1+8))

checked = [
    [0] * (max_r+1) for _ in range(max_r+1)
]

for x1,y1,x2,y2 in rects:
    x1,y1=x1+offset,y1+offset
    x2,y2=x2+offset,y2+offset

    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y] = 1

area=0
for i in range(max_r+1):
    for j in range(max_r+1):
        if checked[i][j] == 1:
            area += 1

print(area)
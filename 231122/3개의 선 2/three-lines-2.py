from itertools import combinations
import sys

n = int(input())
points = []
xp = []
yp = []
tp = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    xp.append(('x', x))
    yp.append(('y', y))

xp = list(set(xp))
yp = list(set(yp))
tp = xp + yp

temp = list(combinations(tp, 3))
found = False

for t in temp:
    cnt = n
    for xory, p in t:
        for point in points:
            if point[0] == p or point[1] == p:
                cnt -= 1

    if cnt == 0:
        found = True
        break

if found:
    print("1")
else:
    print("0")
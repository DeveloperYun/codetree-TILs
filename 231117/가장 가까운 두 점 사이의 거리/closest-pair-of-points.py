n=int(input())
points=[]
for i in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

answer=100000
def dist(a,b):
    x1,y1 = a
    x2,y2 = b

    return abs(x2-x1)**2 + abs(y2-y1)**2

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        
        temp = dist(points[i],points[j])

        if temp < answer:
            answer = temp

print(answer)
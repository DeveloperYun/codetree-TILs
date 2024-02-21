n,m=map(int,input().split())

points=[]
for _ in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

answer = 9999999

#points 에서 m 개를 선택해서
#선택된 점 중 가장 거리가 먼 두 점 사이의 거리가
#최소가 되는 프로그램
def dist(p1,p2):
    x1,y1 = p1
    x2,y2 = p2

    return (x1-x2)**2 + (y1-y2)**2

def calc(select):
    temp = 999999

    for i in range(m-1):
        for j in range(i+1,m):
            temp = min(temp, dist(select[i],select[j]))
    return temp


select=[]
def choose(curr, cnt):
    global answer

    if curr == n:
        if cnt == m:
            answer = min(answer,calc(select))
        return
    
    select.append(points[curr])
    choose(curr+1,cnt+1)
    select.pop()

    choose(curr+1,cnt)


choose(0,0)
print(answer)
import math
n=int(input())

points=[]
for _ in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

def solution(a,b,c):
    x1,y1=points[a]
    x2,y2=points[b]
    x3,y3=points[c]
    t = 0
    #한 면은 x축에 평행 y축에 평행
    if (y1==y2 or y1==y3 or y2==y3) and (x1==x2 or x2==x3 or x1==x3):
        t = 0.5*abs((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3))
    
    return t
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            temp = solution(i,j,k)

            if temp > ans:
                ans = temp

print(math.ceil(ans)*2)
n=int(input())
points=[]

for _ in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

dic_p = {}
for i in range(n):
    if points[i][0] not in dic_p:
        dic_p[points[i][0]] = [points[i][1]]
    else:
        dic_p[points[i][0]].append(points[i][1])

answer=0
for key,value in dic_p.items():
    x=min(value)
    answer += x
print(answer)
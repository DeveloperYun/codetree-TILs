x,y=map(int,input().split())

answer=0
for i in range(x,y+1):
    temp = list(map(int,list(str(i))))
    
    if sum(temp) > answer:
        answer = sum(temp)

print(answer)
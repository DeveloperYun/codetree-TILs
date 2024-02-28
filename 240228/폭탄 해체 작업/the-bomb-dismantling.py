n=int(input())
bombs=[]
maxtime = 0

for _ in range(n):
    score, time = map(int,input().split())
    maxtime = max(maxtime,time)
    bombs.append([score,time])

bombs.sort(key=lambda x:x[1])


answer=0
for i in range(1,maxtime+1):
    for j in range(len(bombs)):
        sc,ti = bombs[j]
        ti -= 1
        bombs[j] = [sc,ti]
    
    temp=[]
    for j in range(len(bombs)):
        sc,ti = bombs[j]

        if ti == 0:
            temp.append(sc)
            bombs[j] = [-1,-1]
    
    if temp:
        get = max(temp)
        answer += get
        bombs = [item for item in bombs if item != [-1,-1]]

print(answer)
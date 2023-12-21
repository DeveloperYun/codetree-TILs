n=int(input())
gugu={}
for _ in range(n):
    a,b=map(int,input().split())
    
    if a not in gugu:
        gugu[a] = []
        gugu[a].append(b)
    else:
        gugu[a].append(b)
        


answer=0

for g in gugu.items():
    num, get = g
    if len(get) > 1:
        for i in range(1,len(get)):
            if get[i] != get[i-1]:
                answer += 1

print(answer)
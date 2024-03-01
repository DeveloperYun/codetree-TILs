c,n=map(int,input().split())

red=[]
for _ in range(c):
    x=int(input())
    red.append(x)

black=[]
for _ in range(n):
    a,b = map(int,input().split())
    black.append((a,b))

red.sort()
black.sort()
answer=0

idx=0
while idx<c:
    num = red[idx]

    for i in range(len(black)):
        if black[i][0] <= num <= black[i][1]:
            idx += 1
            answer+=1
            black.remove(black[i])
            break
    else:
        idx+=1
print(answer)
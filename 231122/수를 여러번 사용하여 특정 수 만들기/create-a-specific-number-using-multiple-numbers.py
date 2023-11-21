a,b,c=map(int,input().split())
answer=0

for i in range(1,1000):
    for j in range(1,1000):
        if a*i + b*j <= c:
            answer = max(answer,a*i + b*j)

print(answer)
a,b,c=map(int,input().split())
answer=0

for i in range(1001):
    for j in range(1001):
        if a*i + b*j <= c:
            answer = max(answer,a*i + b*j)

print(answer)
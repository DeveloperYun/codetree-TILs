n=int(input())
data=[]
for _ in range(n):
    a,b=map(int,input().split())
    data.append((a,b))
def solution(x):
    for i in range(n):
        if data[i][0] <= 2**(i+1)*x and 2**(i+1)*x <= data[i][1]:
            continue
        else:
            return False
    return True
answer=[]
for x in range(1,100001):
    if solution(x):
        answer.append(x)
print(min(answer))
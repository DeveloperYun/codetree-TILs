n,m=map(int,input().split())

s=[]
for i in range(n):
    x=input()
    s.append(x)
answer=0
for i in range(m):
    x=input()
    if x in s:
        answer += 1
print(answer)
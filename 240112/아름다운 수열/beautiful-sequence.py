n=int(input())
a=[ int(input()) for _ in range(n)]
m=int(input())
b=[ int(input()) for _ in range(m)]

answer=[]
cnt=0
for i in range(n-m+1):
    # i = 0,1,2,3
    sorta = sorted(a[i:i+m])
    sortb = sorted(b)
    
    if sorta == sortb:
        cnt += 1
        answer.append(i+1)
    elif abs(sorta[0]-sortb[0]) == abs(sorta[1]-sortb[1]) \
    == abs(sorta[2]-sortb[2]):
        cnt += 1
        answer.append(i+1)

print(cnt)
for i in range(cnt):
    print(answer[i])
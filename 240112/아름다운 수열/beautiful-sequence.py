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
    elif abs(sorta[0]-sortb[0]) == abs(sorta[1]-sortb[1]):
        for j in range(m-1):
            if abs(sorta[j]-sortb[j]) != abs(sorta[j+1]-sortb[j+1]):
                break
        else:
            cnt += 1
            answer.append(i+1)

print(len(answer))
for i in range(cnt):
    print(answer[i])
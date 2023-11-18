n,b=map(int,input().split())
p=[]
for i in range(n):
    s=int(input())
    p.append(s)

#예산 = b
#학생i가 원하는 선물의 가격 p[i]
#모든 선물을 반값해서 전수조사
answer=0
p.sort() #2 4 6 8 12
for i in range(n):
    cnt=0
    balance=b
    for j in range(n):
        sales = 0
        if i==j:
            sales = p[j] // 2
        else:
            sales = p[j]

        if balance >= sales:
            balance -= sales
            cnt += 1
    
    answer = max(answer, cnt)

print(answer)
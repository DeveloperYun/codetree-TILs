n,m=map(int,input().split())
sequence=list(map(int,input().split()))

answer = 0
for i in range(n):
    tot = sequence[i]

    for j in range(m-1): #3번 반복
        k = sequence[i] #5
        tot += sequence[k-1]


    answer = max(answer,tot)
print(answer+1)
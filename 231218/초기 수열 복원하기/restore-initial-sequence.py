n=int(input())
array=list(map(int,input().split()))
answer=[]

for i in range(n):
    success=True
    temp=[0 for _ in range(n)]
    temp[0]=i+1
    for j in range(n-1):
        if abs(array[j]-temp[j]) in temp:
            success=False
            break
        temp[j+1]=abs(array[j]-temp[j])

    if success:
        answer.append(temp)

answer=sorted(answer)
print(*answer[0])
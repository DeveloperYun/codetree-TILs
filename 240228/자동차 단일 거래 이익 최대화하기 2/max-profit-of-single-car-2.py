n=int(input())
arr=list(map(int,input().split()))

answer=0

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] < arr[j]:
            answer = max(answer,arr[j]-arr[i])
        else:
            continue
print(answer)
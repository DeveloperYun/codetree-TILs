n,k=map(int,input().split())
arr=[]
for i in range(n):
    t=int(input())
    arr.append(t)

answer=[]
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            if j-i <= k:
                answer.append(arr[i])

print(max(answer))
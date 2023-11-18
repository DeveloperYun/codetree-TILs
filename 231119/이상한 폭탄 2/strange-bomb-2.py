n,k=map(int,input().split())
arr=[]
for i in range(n):
    t=int(input())
    arr.append(t)

answer=[]
for i in range(n):
    for j in range(n):
        if arr[i] == arr[j]:
            if j-i <= k:
                answer.append(arr[i])

print(max(answer))
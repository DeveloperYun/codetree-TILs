from itertools import combinations

n,k=map(int,input().split())
arr=[]
for i in range(n):
    s=int(input())
    arr.append(s)

arr.sort()
answer = 0

for i in range(n):
    for j in range(i, n):
        if arr[j] - arr[i] <= k:
            answer = max(answer, j-i+1)
            

print(answer)
from itertools import combinations

n,k=map(int,input().split())
arr=[]
for i in range(n):
    s=int(input())
    arr.append(s)

answer = []

data=[]
for i in range(1,n+1):#1~5
    temp = list(combinations(arr,i))
    data.append(temp)

for d in data:
    # d = [(1, 6), (1, 4), (1, 3), (1, 1), (6, 4), (6, 3), (6, 1), (4, 3), (4, 1), (3, 1)]
    for i in d:
    
        max_t = max(i)
        min_t = min(i)

        temp = max_t-min_t

        if temp <= k:
            answer.append(len(i))

print(max(answer))
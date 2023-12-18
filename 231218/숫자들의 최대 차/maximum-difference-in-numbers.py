from itertools import combinations

n,k=map(int,input().split())
arr=[]
for i in range(n):
    s=int(input())
    arr.append(s)

answer = []

for i in range(1,n+1):#1~5
    temp = list(combinations(arr,i))
    # temp = [(1, 6, 4, 3), (1, 6, 4, 1), (1, 6, 3, 1), (1, 4, 3, 1), (6, 4, 3, 1)]
    for d in temp:
        # d = (1,6,4,3)
        max_t = max(d)
        min_t = min(d) 

        temp = max_t-min_t

        if temp <= k:
            answer.append(len(d))
            

print(max(answer))
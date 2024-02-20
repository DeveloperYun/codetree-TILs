from itertools import combinations

n,m=map(int,input().split())
arr=list(map(int,input().split()))

answer = 0

s = list(combinations(arr,m))
for x in s:
    xx=0
    t = x[0]
    for i in range(1,len(x)):
        xx = t ^ x[i]
    
    answer = max(answer,xx)
print(answer)
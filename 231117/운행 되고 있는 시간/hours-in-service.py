n=int(input())
arr=[]
for _ in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))

answer=0

for i in range(n):
    count=[0]*1000
    for j in range(n):
        if i==j:
            continue

        x,y=arr[j]
        for k in range(x,y):
            count[k] = 1
    answer = max(answer, sum(count))

print(answer)
n=int(input())
arr=[]
for _ in range(n):
    s,e=map(int,input().split())
    arr.append((s,e))

arr.sort(lambda x:x[1])
answer=2

for i in range(n-1):
    before_start,before_end = arr[i]
    after_start,after_end = arr[i+1]

    if before_end <= after_start:
        answer += 1
        
print(answer)
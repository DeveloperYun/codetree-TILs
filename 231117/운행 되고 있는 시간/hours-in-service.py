n=int(input())
arr=[]
for _ in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))

answer=0

for i in range(n):
    for j in range(n):
        if i==j:
            continue

        # (3,7) (5,9)
        if arr[i][1] > arr[j][0]:
            t = arr[j][1]-arr[i][0]
        else:
            s1=arr[i][1]-arr[i][0]
            s2=arr[j][1]-arr[j][0]

            t=s1+s2
        if t>answer:
            answer=t

print(answer)
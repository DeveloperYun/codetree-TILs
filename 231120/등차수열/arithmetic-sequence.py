n=int(input())
arr=list(map(int, input().split()))
#k의 최대는 100
k_max=0
for k in range(1, 101):
    cnt=0
    for i in range(n):
        for j in range(i, n):
            if (arr[i]+arr[j])/2==k:
                cnt+=1
    k_max=max(k_max, cnt)
print(k_max)
n=int(input())
arr=list(map(int,input().split()))

ans=0
for i in range(n):

    if ans < 0:
        ans = arr[i]
    else:
        ans += arr[i]

print(ans)
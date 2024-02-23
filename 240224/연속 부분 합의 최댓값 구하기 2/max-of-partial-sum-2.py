n=int(input())
arr=list(map(int,input().split()))

ans=0
for i in range(n):
    ans += arr[i]
    if i==n-1:
        break
    if ans < 0:
        ans = 0

print(ans)
n=int(input())
arr=list(map(int,input().split()))

ans=0
for i in range(n):
    ans += arr[i]
    
    if ans < arr[i]:
        ans = arr[i]
print(ans)
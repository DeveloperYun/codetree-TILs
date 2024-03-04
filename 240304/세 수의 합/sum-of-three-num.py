from itertools import combinations

n,k=map(int,input().split())
arr=list(map(int,input().split()))
n2 = [x for x in range(n)]
#n개중 3개를 골라 더했을 때 k가 되는 경우의 수 
s = list(combinations(n2,3))

ans=0
for idx in s:
    a,b,c = idx
    if arr[a]+arr[b]+arr[c] == k:
        ans += 1

print(ans)
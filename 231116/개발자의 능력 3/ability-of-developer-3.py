s=list(map(int,input().split()))
n=6

def get_diff(i,j,k):
    sum1 = s[i]+s[j]+s[k]
    sum2 = sum(s) - sum1
    return abs(sum1-sum2)

min_diff=1000001
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            min_diff = min(min_diff, get_diff(i,j,k))

print(min_diff)
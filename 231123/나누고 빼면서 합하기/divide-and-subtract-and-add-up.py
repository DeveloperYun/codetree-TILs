n,m=map(int,input().split())
a=list(map(int,input().split()))

answer=a[m-1]
while m>1:

    

    if m%2!=0:
        m-=1
    else:
        m//=2
    answer += a[m-1]
print(answer)
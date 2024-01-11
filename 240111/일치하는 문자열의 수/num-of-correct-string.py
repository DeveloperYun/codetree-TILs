a,b=map(str,input().split())
a=int(a)
cnt=0
for i in range(a):
    t=input()
    if b==t:
        cnt+=1
print(cnt)
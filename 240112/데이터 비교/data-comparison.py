n=int(input())
s=list(map(int,input().split()))
m=int(input())
s2=list(map(int,input().split()))

set1 = set(s)
set2 = set(s2)
l=[]
no = False

for elem2 in s2:
    if elem2 in set1:
        l.append(1)
    else:
        l.append(0)

for i in range(len(l)):
    print(l[i],end=" ")
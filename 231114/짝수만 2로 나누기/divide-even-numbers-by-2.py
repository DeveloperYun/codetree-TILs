n=int(input())
m=list(map(int,input().split()))

def answer(lst):
    ans=[]
    for i in lst:
        if i%2==0:
            ans.append(i//2)
        else:
            ans.append(i)
    
    return ans

t=answer(m)
for i in t:
    print(i,end=" ")
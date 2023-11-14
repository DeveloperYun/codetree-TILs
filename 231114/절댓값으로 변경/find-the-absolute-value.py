n=int(input())
s=list(map(int,input().split()))

def answer(s):
    ans=[]
    for i in s:
        if i < 0:
            ans.append(abs(i))
        else:
            ans.append(i)

    for i in ans:
        print(i,end=" ")
answer(s)
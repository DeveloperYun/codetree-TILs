n=int(input())
arr=list(map(int,input().split()))
answer = 999999

def calc(a,b):
    sa, sb = sum(a), sum(b)
    return abs(sa-sb)

select=[]
def search(idx,cnt):
    global answer
    if idx == 2*n:
        if cnt==n:
            s2 = [] #arr - select 
            for x in arr:
                if x not in select:
                    s2.append(x)
            answer = min(answer,calc(select,s2))
        return
    
    select.append(arr[idx])
    search(idx+1,cnt+1)
    select.pop()

    search(idx+1,cnt)

search(0,0)
print(answer)
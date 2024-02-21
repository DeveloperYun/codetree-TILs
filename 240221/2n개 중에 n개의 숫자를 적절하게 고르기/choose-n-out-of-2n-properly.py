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
            temp = arr[:]
            s2 = [] #arr - select 
            for i in range(n):
                for j in range(2*n):
                    if select[i] == temp[j]:
                        temp[j]=0
            for i in temp:
                if i==0:
                    temp.remove(i)
            answer = min(answer,calc(select,s2))
        return
    
    select.append(arr[idx])
    search(idx+1,cnt+1)
    select.pop()

    search(idx+1,cnt)

search(0,0)
print(answer)
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
            s2 = [] #temp - select 
            #temp : 1,1,2,4
            #select : 1,2
            for i in range(n):
                for j in range(len(temp)):
                    if select[i] == temp[j]:
                        temp.pop(j)
                        break
            answer = min(answer,calc(select,temp))
        return
    
    select.append(arr[idx])
    search(idx+1,cnt+1)
    select.pop()

    search(idx+1,cnt)

search(0,0)
print(answer)
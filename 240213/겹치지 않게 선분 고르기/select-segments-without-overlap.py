n=int(input())
array=[list(map(int,input().split())) for _ in range(n)]

answer=0
select=[]

def is_possible():
    for idx1,value1 in enumerate(select):
        for idx2,value2 in enumerate(select):
            x1,y1=value1
            x2,y2=value2
            if idx1<idx2 and (x1<=x2<=y1 or x1<=y2<=y1 or x2<=x1<y2 or x2<=y1<=y2):
                return False
    return True

# x1 y1 x2 y2
# x2 y2 x1 y1

def func(cnt,num):
    global answer
    if cnt>n:
        return
    if num>n:
        return
    if is_possible():
        #print("func(",cnt+1,",",num,")")
        #print(select)
        answer=max(answer,len(select))

    for i in range(num,n):
        select.append(array[i])
        func(cnt+1,i+1)
        select.pop()

func(0,0)
print(answer)
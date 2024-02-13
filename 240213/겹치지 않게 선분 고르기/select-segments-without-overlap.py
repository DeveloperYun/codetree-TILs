n=int(input())
arr=[]
for _ in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))

answer=0
arr.sort()

select = []

def check():
    a = list(set(select))
    temp = len(a)
    if len(a) > 1:
        for i in range(len(a)-1):
            if (a[i+1][0] >= a[i][0] and a[i+1][1] >= a[i][1]) or (a[i][0] >= a[i+1][0] and a[i][1] <= a[i+1][1]):
                temp -= 1
        return temp 
    else:
        return 1


def recur(num):
    global answer
    if num==n:
        answer = max(answer, check())
        return 
    
    for i in range(n):
        select.append(arr[i]) 
        recur(num+1)
        select.pop()
        

recur(0)    
print(answer)
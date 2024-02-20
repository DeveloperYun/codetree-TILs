n=int(input())
arr=list(map(int,input().split()))

answer = 999
step=[]
def find_min(idx):
    global answer

    if idx == n-1:
        answer = min(answer, len(step))
        return
    
    for i in range(1,arr[idx]+1):
        if 0<= idx + i <= n-1:
            step.append(i)
            find_min(idx + i)
            step.pop()

find_min(0)
if answer == 999: print(-1)
else: print(answer)
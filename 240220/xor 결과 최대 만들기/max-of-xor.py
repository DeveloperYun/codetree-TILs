n,m=map(int,input().split())
arr=list(map(int,input().split()))

answer = 0
take=[]

def compute():
    answer=0
    for elem in take:
        answer ^= elem
    
    return answer

def xor(cur,cnt):
    global answer

    # arr에서 m개를 뽑아서 xor 한다.
    if cur == n:
        if cnt == m:
            answer = max(answer, compute())
        return

    take.append(arr[cur]) #cur 위치의 값을 선택
    xor(cur+1, cnt+1)
    take.pop()

    xor(cur+1,cnt) #선택x 

xor(0,0)
print(answer)
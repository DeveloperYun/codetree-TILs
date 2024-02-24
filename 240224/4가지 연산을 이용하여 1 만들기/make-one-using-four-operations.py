from collections import deque

n=int(input())

q=deque()
visited=[]

def push(n, cnt):
    global q,visited

    visited.append(n) #나온 숫자를 저장
    q.append((n,cnt))

push(n,0)
answer=0

while q:
    curr, cnt = q.popleft()

    if curr == 1:
        answer = cnt
        break
    
    if (curr - 1) not in visited:
        push(curr-1, cnt+1)
    
    if (curr + 1) not in visited:
        push(curr+1, cnt+1)
    
    if (curr%2==0) and (curr%2) not in visited:
        push(curr//2, cnt+1)

    if (curr%3==0) and (curr%3) not in visited:
        push(curr//3, cnt+1)

print(answer)
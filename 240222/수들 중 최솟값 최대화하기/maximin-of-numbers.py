n=int(input())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

select=[]
visited = [False]*n
answer=0

def choose(cnt):
    global answer

    if cnt==n:
        tm = min(select)
        answer = max(answer,tm)
        return

    for col in range(n):
        if visited[col]:
            continue

        visited[col] = True #방문
        select.append(grid[cnt][col])
        choose(cnt+1)
        select.pop()
        visited[col] = False
    
choose(0)
print(answer)
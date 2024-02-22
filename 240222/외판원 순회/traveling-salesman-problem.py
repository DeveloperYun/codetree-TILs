n=int(input())
grid=[
    list(map(int,input().split()))
    for _ in range(n)
]

visited=[False]*n
answer=99999999
temp = []

def choose(curr):
    global answer

    if curr == n:
        answer = min(answer,sum(temp))
        return 

    
    for col in range(n):
        if visited[col] or grid[curr][col]==0:
            continue
        
        visited[col] = True

        temp.append(grid[curr][col])
        choose(curr+1)
        temp.pop()
        visited[col] = False

choose(0)
print(answer)
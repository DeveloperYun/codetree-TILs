n=int(input())
visited = [False]*(1+n)

answer=[]

def pt():
    for t in answer:
        print(t,end=' ')
    print()

def choose(curr):
    if curr == n+1:
        pt()
        return
    
    for i in range(n,0,-1):
        if visited[i]:
            continue

        visited[i] = True
        answer.append(i)

        choose(curr+1)
        answer.pop()
        visited[i] = False
    
choose(1)
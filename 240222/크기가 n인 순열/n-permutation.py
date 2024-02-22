n=int(input())

visited = [False]*(1+n)
answer=[]

def pt():
    for e in answer:
        print(e,end=' ')
    print()

def choose(curr):
    if curr == n+1:
        pt()
        return

    for i in range(1,n+1):
        if visited[i]: 
            continue
        
        visited[i] = True
        answer.append(i)

        choose(curr+1)

        answer.pop()
        visited[i] = False

choose(1)
N, M = map(int, input().split())

def choose(n, prev):

    if n == M+1:
        for e in l:
            print(e, end=' ')
        print()
        return
    
    for i in range(1, N+1):
        
        if i > prev:
            l.append(i)
            choose(n+1, i)
            l.pop()

    return 

l = []
choose(1, 0)
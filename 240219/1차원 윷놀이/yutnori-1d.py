n,m,k=map(int,input().split())
#턴의 수 n
#판의 상태 m
#말의 수 k 
board = [x for x in range(1,m+1)]
dist = list(map(int,input().split()))

#board = [1, 2, 3, 4, 5, 6]
answer = 0
selected_number = []

def calc(selected):
    #dist = [2,4,2,4]
    #selected = [3,3,2,1]
    member = [1]*k #[1,1,1]
    score=0

    for i in range(n):
        member[selected[i]] += dist[i]
    
    for i in member:
        if i >= m:
            score += 1
    return score

def find(idx):
    global answer
    if idx == n:
        sc = calc(selected_number)
        answer = max(answer, sc)
        return

    for i in range(k):
        selected_number.append(i)
        find(idx+1)
        selected_number.pop()

find(0)
print(answer)
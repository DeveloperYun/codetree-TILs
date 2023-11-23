from collections import deque

n, k = list(map(int ,input().split()))

arr=[
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = list(map(int, input().split()))

temp = [
    [e for e in row]
    for row in arr
]

visited=[
    [0 for _ in range(n)]
    for _ in range(n)
]

q = deque()

def initialization():
    global temp
    global visited

    temp = [
        [e for e in row]
        for row in arr
    ]

    visited=[
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    q = deque()


def in_range(y, x):
    return 0<=y and y<n and 0<=x and x<n


def can_go(y, x):
    global temp
    return in_range(y, x) and not visited[y][x] and temp[y][x]

def bfs():

    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]

    while q:
        y, x = q.popleft()
        

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if can_go(ny, nx):
                q.append((ny, nx))
                visited[ny][nx] = 1


def find_next(y, x):
    global temp
    global visited
    global q

    candidates=[]

    e = temp[y][x]
    for j in range(n):
        for i in range(n):
            if temp[j][i] >= e:
                temp[j][i] = 0
    
    q.append((y, x))
    bfs()

    for j in range(n):
        for i in range(n):
            if visited[j][i]:
                candidates.append((temp[j][i], j, i))
    
    candidates.sort(key = lambda x: (-x[0], x[1], x[2]))
    initialization()
    return candidates[0][1], candidates[0][2]

r -= 1
c -= 1
y, x = r, c

for _ in range(k):
    y, x = find_next(y, x)

print(y+1, x+1)
n, m, t = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

count = [[0]*n for _ in range(n)]
for _ in range(m) :
    x, y = map(int, input().split())
    count[x-1][y-1] = 1

def in_range(x, y) :
    return 0<=x<n and 0<=y<n

def next_pos(x, y) :
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    max_num = 0
    max_pos = (-1, -1)

    for dx, dy in zip(dxs, dys) :
        next_x, next_y = x + dx, y + dy
        if in_range(next_x, next_y) and arr[next_x][next_y] > max_num :
            max_num = arr[next_x][next_y]
            max_pos = (next_x, next_y)

    x, y = max_pos
    return x, y

def simulate() :
    tmp_count = [[0]*n for _ in range(n)]
    global count
    for i in range(n) :
        for j in range(n) :
            if count[i][j] == 1 :
                x, y = next_pos(i, j)
                tmp_count[x][y] += 1

    count = tmp_count

def boom() :
    for i in range(n) :
        for j in range(n) :
            if count[i][j] >= 2 :
                count[i][j] = 0

     
for _ in range(t) :
    simulate()
    boom()

sum = 0 
for i in range(n) :
    for j in range(n) :
        sum += count[i][j]

print(sum)
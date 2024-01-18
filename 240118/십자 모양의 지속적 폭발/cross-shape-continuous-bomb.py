n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for i in range(n)
]

bomb_list = [
    int(input()) - 1
    for _ in range(m)
]

d_rows = [-1, 0, 1, 0]
d_cols = [0, 1, 0, -1]

def drop():
    for col in range(n):
        temp = []
        for i in range(n-1, -1, -1):
            num = grid[i][col]
            if num:
                temp.insert(0, num)
        while len(temp) < n:
            temp.insert(0, 0)
        
        for i in range(n):
            grid[i][col] = temp[i]

def in_range(row, col):
    if row < 0 or n <= row:
        return False
    if col < 0 or n <= col:
        return False
    return True

def bomb(row, col):
    l = grid[row][col]
    grid[row][col] = 0
    for d_row, d_col in zip(d_rows, d_cols):
        t_row = row
        t_col = col
        for _ in range(l - 1):
            n_row = t_row + d_row
            n_col = t_col + d_col

            if not in_range(n_row, n_col):
                break
            
            grid[n_row][n_col] = 0

            t_row = n_row
            t_col = n_col
    drop()


for col in bomb_list:
    for row in range(n):
        if grid[row][col]:
            bomb(row, col);
            break;


for row in range(n):
    print(" ".join(map(str, grid[row])))
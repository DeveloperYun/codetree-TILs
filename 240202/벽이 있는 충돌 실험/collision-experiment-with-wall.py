MAX_N = 50

t = int(input())
dir_map = {
    'U': 0,
    'D': 3,
    'L': 1,
    'R': 2
}

grid = [
    [0 for _ in range(MAX_N)]
    for _ in range(MAX_N)
]


def in_range(row, col):
    return 0 <= row < grid_size and 0 <= col < grid_size


def move(x, y, d):
    dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]
    nx, ny = x + dxs[d], y + dys[d]

    if in_range(nx, ny):
        return nx, ny, d
    else:
        return x, y, 3 - d


def init_grid(next_marbles_set):
    for x, y, _ in next_marbles_set:
        grid[x][y] = 0


def move_all():
    next_marbles_set = set()

    for x, y, d in marbles:
        nx, ny, d = move(x, y, d)
        grid[nx][ny] += 1
        next_marbles_set.add((nx, ny, d))

    return next_marbles_set


def check_dupl(next_marbles_set):
    global marbles
    cnt = 0
    next_marbles = []
    for x, y, d in next_marbles_set:
        if grid[x][y] == 1:
            next_marbles.append((x, y, d))
            cnt += 1
            
    marbles = next_marbles
    return cnt


def simulate():
    for _ in range(2 * grid_size):
        next_marbles_set = move_all()
        ans = check_dupl(next_marbles_set)
        init_grid(next_marbles_set)

    print(ans)


for _ in range(t):
    grid_size, m = tuple(map(int, input().split()))
    marbles = []

    for _ in range(m):
        char_x, char_y, char_dir = tuple(input().split())
        x, y, d = int(char_x) - 1, int(char_y) - 1, dir_map[char_dir]
        marbles.append((x, y, d))

    simulate()
def check_repeat(grid, m):
    boom_range = set()

    for j in range(len(grid[0])):
        start, end, repeat_count = 0, 0, 1

        for i in range(len(grid) - 1):
            if grid[i][j] == grid[i + 1][j]:
                end += 1
                repeat_count += 1
                if repeat_count >= m:
                    boom_range.add((start, end))
            else:
                if repeat_count >= m:
                    boom_range.add((start, end))
                start, end, repeat_count = i + 1, i + 1, 1

        for x, y in boom_range:
            for k in range(x, y + 1):
                grid[k][j] = 0

def gravity(grid):
    for j in range(len(grid[0])):
        for i in range(len(grid) - 2, -1, -1):
            if grid[i][j] != 0:
                k = i
                while k + 1 < len(grid) and grid[k + 1][j] == 0:
                    grid[k + 1][j] = grid[k][j]
                    grid[k][j] = 0
                    k += 1

def rotate(grid):
    return [list(row) for row in zip(*grid[::-1])]

def bomb_simulation(grid, m, k):
    for _ in range(k):
        check_repeat(grid, m)
        gravity(grid)
        check_repeat(grid, m)
        grid = rotate(grid)

    count = sum(row.count(0) for row in grid)
    return len(grid) * len(grid[0]) - count

def main():
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    result = bomb_simulation(grid, M, K)
    print(result)

if __name__ == "__main__":
    main()
def explode(grid, r, c):
    size = grid[r][c]
    grid[r][c] = 0

    for i in range(1, size):
        if r - i >= 0:
            grid[r - i][c] = 0  # 위쪽
        if r + i < n:
            grid[r + i][c] = 0  # 아래쪽
        if c - i >= 0:
            grid[r][c - i] = 0  # 왼쪽
        if c + i < n:
            grid[r][c + i] = 0  # 오른쪽

def apply_gravity(grid):
    for col in range(n):
        non_zero_elements = [grid[row][col] for row in range(n) if grid[row][col] != 0]
        zeros_count = n - len(non_zero_elements)
        non_zero_elements = [0] * zeros_count + non_zero_elements
        for row in range(n):
            grid[row][col] = non_zero_elements[row]

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

# 입력 받기
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
explode_position = tuple(map(int, input().split()))

# 폭발 및 중력 적용
explode(grid, explode_position[0] - 1, explode_position[1] - 1)
apply_gravity(grid)

# 결과 출력
print_grid(grid)
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end=" ")
        print()

# 폭발
def explode():
    explode_count = 0

    for col in range(N):
        count, st = 0, 0
        ranges_to_explode = []

        for row in range(N):
            # 끊기는 순간을 판단
            if grid[row][col] == 0 or (row and grid[row][col] != grid[row - 1][col]):
                if count >= M:
                    ranges_to_explode.append((st, row - 1))
                
                # 값 초기화
                count, st = 0, 0
            
            # 현재 칸이 정상적인 칸이라면
            # 개수 갱신
            if grid[row][col] != 0:
                count += 1
                
                if count == 1:
                    st = row

        # 마지막 그룹은 따로 처리해주어야 함.
        # 현재 방식대로라면 열 첫번째 원소가 0일때도 range가 (0, 0)으로 잡힘 -> 예외처리
        if count >= M:
            ranges_to_explode.append((st, N - 1))


        for start, end in ranges_to_explode:
            for row in range(start, end+1):
                explode_count += 1
                grid[row][col] = 0

    return explode_count


# 중력 작용
def pull_down():
    for col in range(N):
        temp = []
        for row in range(N):
            if grid[row][col]:
                temp.append(grid[row][col])

        # 떨어뜨릴게 없다면 해당 열은 패스
        if len(temp) == N:
            continue

        buff = [0 for _ in range(N-len(temp))]
        temp = buff + temp

        for row in range(N):
            grid[row][col] = temp[row]

# 시계방향으로 배열 회전
def rotate():
    global grid
    next_grid = [[0 for _ in range(N)] for __ in range(N)]

    for i in range(N):
        for j in range(N):
            next_grid[i][j] = grid[N-j-1][i]

    grid = next_grid

def get_count():
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                count += 1
    return count

def main():
    for _ in range(K):
        while True:
            if explode() == 0:
                break
            pull_down()
        rotate()
        pull_down()

    # 회전을 반복한 후에도 터질게 있다면 터져야 함
    while True:
        if explode() == 0:
            break
        pull_down()

    print(get_count())


main()
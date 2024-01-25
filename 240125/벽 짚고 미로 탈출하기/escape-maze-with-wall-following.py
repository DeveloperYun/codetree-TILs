n = int(input())
x, y = tuple(map(int, input().split()))
x, y = x - 1, y - 1

arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    a = input()
    for j, elem in enumerate(a):
        arr[i][j] = elem

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 배열 범위
def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

# 움직이기
def move():
    global cur

    # 사방이 막혔을 경우를 확인하기 위한 변수
    cnt = 0
    for _ in range(4):
        cnt += 1
        nx, ny = x + dxs[cur], y + dys[cur]
        # 밖으로 나갈 수 있다면
        if not in_range(nx, ny):
            return (-1, -1)
        else:
            # 진행방향에 벽이 있다면
            if arr[nx][ny] == '#':
                # 반 시계 방향 90도 회전
                cur = (cur + 3) % 4
            # 진행방향으로 갈 수 있다면
            elif arr[nx][ny] == '.':
                # 움직이기
                break

    return (nx, ny) if cnt != 4 else (x, y)

# 진행방향 기준 오른쪽에 벽이 존재하는지 검사하는 함수
def check():
    right = (cur + 1) % 4

    nx, ny = x + dxs[right], y + dys[right]
    # 오른쪽에 벽이 있는 경우
    if arr[nx][ny] == '#':
        return True
    # 오른쪽에 벽이 없는 경우
    else:
        return False


cur = 0 # 시작 진행 방향
result = 0

for _ in range(n * n):
    # 진행하기
    pos = move()
    result += 1
    
    # 밖으로 나갔다면 반복 종료
    if pos == (-1, -1):
        break
    
    x, y = pos
    # 진행 방향 기준 오른쪽에 벽 유무 확인
    # 벽이 없다면 진행방향 바꾸기
    if not check():
        cur = (cur + 1) % 4

        
print(result if result != n * n else -1)
n = int(input())

# 범위체크
def in_range(row, col):
    return 0 <= row < n and 0 <= col < n

# 움직일 좌표들
d_map = [
    (0, 0),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1)
] 

# 입력된 숫자를 담고있는 격자
input_num_grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 입력된 방향을 담고있는 격자
input_d_grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 숫자와 방향을 가지고 있는 객체
class Move:
    def __init__(self, num, d):
        self.num = num
        self.d = d

# Move를 담고있느 격자
move_grid = [
    [
        Move(input_num_grid[row][col], d_map[input_d_grid[row][col]])
        for col in range(n)
    ]
    for row in range(n)
]

# 입력된 좌표
input_row, input_col = map(lambda x: int(x) - 1, input().split())

# 최대 숫자를 구하는 함수
def get_max_move_cnt():

    # 최대 숫자를 담는 변수
    max_cnt = 0

    # get_max_move_cnt의 부분함수
    def _get_max_move_cnt(row=input_row, col=input_col, cnt=0):
        nonlocal max_cnt

        # 지금 무브
        move = move_grid[row][col]

        # 다음 무브들을 담는 리스트
        _move_coords = []

        # 다음 무브의 좌표
        _row, _col = row + move.d[0], col + move.d[1]

        # 다음 무브의 좌표가 범위안인 동안반복
        while in_range(_row, _col):
            # 다음 무브
            _move = move_grid[_row][_col]

            # 무브의 숫자가 지금 무브의 숫자보다 크면 _move_coords에 해당 좌표를 추가
            if _move.num > move.num:
                _move_coords.append((_row, _col))
            
            # 뱡향의 다음 위치로 좌표들을 이동
            _row += move.d[0]
            _col += move.d[1]

        # 다음 좌표들이 없다면 값으로 max_cnt를 비교해서 넣어주고 리턴
        if not len(_move_coords):
            max_cnt = max(max_cnt, cnt)
            return
        
        # 다음 좌표들이 있다면 다음 좌표들로 부분함수를 재귀적으로 호출
        for _row, _col in _move_coords:
            _get_max_move_cnt(_row, _col, cnt + 1)
        
    # 부분함수 호출
    _get_max_move_cnt()

    # 최대 숫자를 리턴
    return max_cnt

print(get_max_move_cnt())
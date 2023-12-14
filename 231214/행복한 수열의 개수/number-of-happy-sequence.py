# 시뮬레이션 문제

# 변수 선언 입력 받는 부분은 보고 했음
# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

num = 0

# 가로
for i in range(n):
    number = grid[i][0]
    cnt = 0

     # 갯수에 자기 자신이 포함되므로 자기 자신과 비교할 때부터 1이 카운트 된다
    for j in range(n):
        if number == grid[i][j]:
            cnt = cnt + 1
        else:
           # 다음 숫자와 비교하기 위해 number 에 넣어준다
            number = grid[i][j]
            cnt = 1
        if cnt == m:
            num = num + 1
            cnt = 1
            break
        
# 세로
for i in range(n):
    number = grid[0][i]
    cnt = 0

    # 갯수에 자기 자신이 포함되므로 자기 자신과 비교할 때부터 1이 카운트 된다
    for j in range(n):
        if number == grid[j][i]:
            cnt = cnt + 1
        else:
            # 다음 숫자와 비교하기 위해 number 에 넣어준다
            number = grid[j][i]
            cnt = 1
        if cnt == m:
            num = num + 1
            cnt = 1
            break

print(num)
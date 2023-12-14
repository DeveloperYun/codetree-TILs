# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

ans = 0
# 어느 지점에서 시작할지 전부 시도해 봅니다.
# 모든 경우의 수에 대해 최대가 되도록 하는 수를 계산합니다.
for i in range(1, n + 1):
    # 시작점은 i입니다.
    sum_element = 0
    cur = i

    # m번 움직임을 반복합니다.
    for _ in range(m):
        sum_element += arr[cur]
        cur = arr[cur]
    
    ans = max(ans, sum_element)

print(ans)
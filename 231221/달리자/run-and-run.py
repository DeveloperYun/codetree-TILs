def min_moves(n, A, B):
    total_moves = 0

    for i in range(n):
        # 현재 집의 사람 수와 목표 집의 사람 수를 비교하여 이동 거리 계산
        moves = abs(A[i] - B[i])
        total_moves += moves

        # 다음 집으로 이동하면서 현재 집의 사람 수를 업데이트
        if i < n - 1:
            A[i + 1] += A[i] - B[i]

    return total_moves

# 입력 받기
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 결과 출력
result = min_moves(n, A, B)
print(result)
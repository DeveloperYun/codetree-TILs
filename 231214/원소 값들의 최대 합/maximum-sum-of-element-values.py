def find_max_sum(n, m, sequence):
    max_sum = 0

    for start_position in range(1, n + 1):
        current_position = start_position
        moves_left = m
        current_sum = 0

        while moves_left > 0:
            current_sum += sequence[current_position - 1]
            current_position = sequence[current_position - 1]
            moves_left -= 1

        max_sum = max(max_sum, current_sum)

    return max_sum

# 입력 받기
n, m = map(int, input().split())
sequence = list(map(int, input().split()))

# 최대 합 계산 및 출력
result = find_max_sum(n, m, sequence)
print(result)
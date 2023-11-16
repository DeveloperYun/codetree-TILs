def count_unlocked_combinations(N, combination):
    total_combinations = N ** 3  # 모든 조합의 수

    # 조합에서 두 숫자 간의 거리가 2 이내인 경우를 찾아서 제외
    excluded_combinations = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if abs(combination[0] - i) > 2 and abs(combination[1] - j) > 2 and abs(combination[2] - k) > 2:
                    excluded_combinations += 1

    # 가능한 서로 다른 조합의 수 계산
    result = total_combinations - excluded_combinations
    return result

# 입력 받기
N = int(input())
combination = list(map(int, input().split()))

# 결과 출력
print(count_unlocked_combinations(N, combination))
def count_max_pairs(n, m, pairs):
    pair_counts = {}  # Dictionary to store counts of each pair

    # Count occurrences of each pair
    for pair in pairs:
        a, b = min(pair), max(pair)
        pair_counts[(a, b)] = pair_counts.get((a, b), 0) + 1

    # Find the maximum count
    max_count = max(pair_counts.values())

    print(max_count)

# 입력 받기
n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# 함수 호출 및 결과 출력
count_max_pairs(n, m, pairs)
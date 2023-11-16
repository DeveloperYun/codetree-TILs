def min_cost_to_equal_height(heights, target_height, target_count):
    n = len(heights)
    min_cost = float('inf')

    for i in range(n - target_count + 1):
        current_heights = heights[i:i + target_count]
        current_cost = 0

        for h in current_heights:
            current_cost += abs(target_height - h)

        min_cost = min(min_cost, current_cost)

    return min_cost

# 입력 받기
n, target_height, target_count = map(int, input().split())
heights = list(map(int, input().split()))

# 결과 출력
result = min_cost_to_equal_height(heights, target_height, target_count)
print(result)
import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
a, b, x, y = tuple(map(int, input().split()))

min_dist = INT_MAX

# Case 1. a -> b 바로 이동
min_dist = min(min_dist, abs(b - a))

# Case 2. a -> x -> y -> b 순서로 이동
min_dist = min(min_dist, abs(x - a) + 0 + abs(b - y))

# Case 3. a -> y -> x -> b 순서로 이동
min_dist = min(min_dist, abs(y - a) + 0 + abs(b - x))

print(min_dist)
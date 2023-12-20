def max_h_score(N, L, numbers):
    numbers.sort()

    for i in range(L):
        if i < N - 1 and numbers[i] == numbers[i + 1]:
            numbers[i] += 1
            numbers.sort()

    h_score = 0
    for h in range(1, N + 2):
        count = sum(1 for num in numbers if num >= h)
        if count >= h:
            h_score = h

    return h_score

# 입력 처리
N, L = map(int, input().split())
numbers = list(map(int, input().split()))

# 최대 H 점수 계산
result = max_h_score(N, L, numbers)

# 결과 출력
print(result)
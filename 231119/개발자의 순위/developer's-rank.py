def count_strict_pairs(K, N, results):
    count = 0  # 서로 다른 (a, b) 쌍의 수를 세는 변수

    # 모든 개발자 쌍을 확인하여 불변의 순위를 찾음
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a != b:
                strict = True
                # 각 경기에 대해 불변의 순위를 확인
                for k in range(K):
                    if results[k][a - 1] >= results[k][b - 1]:
                        strict = False
                        break
                if strict:
                    count += 1

    return count

# 입력 받기
K, N = map(int, input().split())
results = [list(map(int, input().split())) for _ in range(K)]

# 결과 계산 및 출력
result_count = count_strict_pairs(K, N, results)
print(result_count)
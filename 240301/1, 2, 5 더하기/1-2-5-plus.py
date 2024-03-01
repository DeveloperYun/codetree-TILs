def count_ways(n):
    # 1, 2, 5의 합으로 나타내는 방법의 수를 저장할 배열
    dp = [0] * (n + 1)
    # 초기값 설정
    dp[0] = 1
    
    # 1부터 n까지 각 숫자에 대한 나타내는 방법의 수 계산
    for i in range(1, n + 1):
        # 1을 사용하는 경우
        if i >= 1:
            dp[i] += dp[i - 1]
        # 2를 사용하는 경우
        if i >= 2:
            dp[i] += dp[i - 2]
        # 5를 사용하는 경우
        if i >= 5:
            dp[i] += dp[i - 5]
        # 나머지 연산 수행
        dp[i] %= 10007
    
    return dp[n]

# 입력 받기
n = int(input())

# 결과 출력
print(count_ways(n))
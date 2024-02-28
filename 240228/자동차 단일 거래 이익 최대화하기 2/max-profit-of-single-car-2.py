def maximize_profit(n, prices):
    if n <= 1:
        return 0

    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
        current_price = prices[i]
        max_profit = max(max_profit, current_price - min_price)
        min_price = min(min_price, current_price)

    return max_profit

# 입력 처리
n = int(input())
prices = list(map(int, input().split()))

# 최대 이익 계산 및 출력
result = maximize_profit(n, prices)
print(result)
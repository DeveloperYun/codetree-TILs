n = int(input())  # 정수 n 입력
numbers = list(map(int, input().split()))  # n개의 정수를 리스트로 입력

# 가장 작은 값과 두 개의 가장 큰 값 저장
min1, min2 = float('inf'), float('inf')
max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')

for num in numbers:
    if num <= min1:
        min2 = min1
        min1 = num
    elif num <= min2:
        min2 = num

    if num >= max1:
        max3 = max2
        max2 = max1
        max1 = num
    elif num >= max2:
        max3 = max2
        max2 = num
    elif num >= max3:
        max3 = num

# 최대값을 저장할 변수 초기화
max_product = max(min1 * min2 * max1, max1 * max2 * max3)

# 결과 출력
print(max_product)
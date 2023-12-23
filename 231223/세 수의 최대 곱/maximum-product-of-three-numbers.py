n = int(input())  # 정수 n 입력
numbers = list(map(int, input().split()))  # n개의 정수를 리스트로 입력

# 최대값을 저장할 변수 초기화
max_product = float('-inf')

# 세 숫자를 골라 나올 수 있는 곱 중 최대값 찾기
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            current_product = numbers[i] * numbers[j] * numbers[k]
            max_product = max(max_product, current_product)

# 결과 출력
print(max_product)
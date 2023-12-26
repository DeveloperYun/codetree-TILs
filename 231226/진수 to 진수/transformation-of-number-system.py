def base_conversion(n, base_from, base_to):
    # a진수를 10진수로 변환
    decimal_num = int(str(n), base_from)

    # 10진수를 b진수로 변환
    converted_num = ""
    while decimal_num > 0:
        remainder = decimal_num % base_to
        converted_num = str(remainder) + converted_num
        decimal_num //= base_to

    return converted_num

# 입력 받기
a, b = map(int, input().split())
n = input()

# 변환 함수 호출 및 결과 출력
result = base_conversion(n, a, b)
print(result)
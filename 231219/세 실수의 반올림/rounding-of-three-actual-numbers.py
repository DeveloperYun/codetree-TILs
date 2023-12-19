# 세 개의 실수를 입력 받기
a = float(input())
b = float(input())
c = float(input())

# 각각의 실수를 반올림하여 소수 셋째 자리까지 출력
print("{:.3f}".format(round(a, 3)))
print("{:.3f}".format(round(b, 3)))
print("{:.3f}".format(round(c, 3)))
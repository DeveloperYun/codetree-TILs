# 변수 선언 및 입력
arr = list(map(int, input().split()))

# 주어진 값들을 정렬합니다.
arr.sort()

# Case 1. 3개의 숫자가 전부 연속한 경우
# 이 경우에는 이동할 필요가 없으므로
# 최소 이동 횟수는 0이 됩니다.
if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
    print(0)
# Case 2. 2개의 숫자의 차이가 정확히 2가 나는 경우
# 이 경우에는 남은 숫자를 두 숫자 사이에 바로 넣어주면 되므로
# 최소 이동 횟수는 1이 됩니다.
elif arr[0] + 2 == arr[1] or arr[1] + 2 == arr[2]:
    print(1)
# Case 3. 그렇지 않은 경우에는 항상 2번에 걸쳐
# 3개의 숫자를 연속하게 만드는 것이 가능합니다.
else:
    print(2)
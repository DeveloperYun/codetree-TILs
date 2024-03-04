import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
arr = [0] + list(map(int, input().split()))

# 만들 수 있는 최대 합 m을 계산합니다.
m = sum(arr)

# dp[i][j] : 지금까지 i번째 수까지만 고려해봤을 때,
#            고른 수의 합을 j로 만드는 것이 가능하면 True
#            불가능하면 False
dp = [
    [0] * (m + 1)
    for _ in range(n + 1)
]


def initialize():
    # 초기 조건으로
    # 아직 아무런 수도 고려해보지 않은 상태를 정의합니다.
    # 따라서 지금까지 0번째 수까지 고려해기에
    # 지금까지 선택한 수의 합이 0이므로
    # dp[0][0] = True가 됩니다.
    dp[0][0] = True


initialize()

# 지금까지 i번째 수까지 고려해봤고,
# 지금까지 고른 수들의 합이 j가 되는게 가능한지를 판단합니다.
for i in range(1, n + 1):
    # 이런 상황을 만들기 위한 선택지는 크게 2개 입니다.
    
    # Case 1
    # i번 수를 선택하여 합이 j가 된 경우입니다.
    # 이 경우에는 i번 수를 포함하여 합이 j가 되어야 하므로
    # i - 1번째까지 고려하여 고른 수들의 합이 j - arr[i]였어야 합니다.
    # 단, j < arr[i]인 경우에는 i번째 수를 추가하여 합이 j가 될 수 없으므로
    # j >= arr[i]인 경우에만 가능합니다.

    # Case 2
    # i번 수를 선택하지 않고 합이 j가 된 경우입니다.
    # 이 경우에는 i번 수를 제외하고 합이 j가 되어야 하므로
    # i - 1번째까지 고려하여 고른 수들의 합이 j였어야만 합니다. 
    for j in range(m + 1):
        # Case 1
        if j >= arr[i] and dp[i - 1][j - arr[i]]:
            dp[i][j] = True
        
        # Case 2
        if dp[i - 1][j]:
            dp[i][j] = True

# n개의 수까지 전부 고려했을 때
# 그룹 A에 대해 정확히 합 i를 만들 수 있다면,
# i / m - i 이렇게 두 그룹으로 나눌 수 있다는 뜻이기에
# 차이의 최솟값을 갱신합니다.
ans = INT_MAX
for i in range(1, m):
    if dp[n][i]:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
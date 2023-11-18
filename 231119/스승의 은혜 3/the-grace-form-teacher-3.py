N, B = map(int, input().split())
want = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

# 정렬 기준?
# x[0]//2 + x[1] or x[0]+x[1]
want.sort(key=lambda x:(x[0]+x[1]))

# 할인 쿠폰을 i번째 학생에게 쓰는 경우
ans = -1
for i in range(N):
    money = B
    cnt = 0
    for j in range(N):
        if j == i:
            if money >= want[j][0] // 2 + want[j][1]:
                money -= (want[j][0] // 2 + want[j][1])
                cnt += 1

        else:
            if money >= want[j][0] + want[j][1]:
                money -= (want[j][0] + want[j][1])
                cnt += 1

    ans = max(ans, cnt)

print(ans)
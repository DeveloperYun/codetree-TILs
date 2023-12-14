n = int(input())
string = input()

ans = 1

# 1씩 늘려가면서 어느 길이까지 2번 등장하지는지 모두 시도해봅니다.
for i in range(1, n):
    # 모든 길이가 i인 부분 문자열에 대해 쌍을 짓고
    # 둘이 완전히 똑같은지 확인합니다.

    # twice : i 길이의 2회 이상 등장하는 부분 문자열이 존재하면 true
    twice = False

    for j in range(n - i + 1):
        for k in range(j + 1, n - i + 1):
            # issame : j부터 i길이의 부분 문자열과
            # k부터 i길이의 부분 문자열이 완전히 같으면 true
            issame = True

            for l in range(i):
                if string[j + l] != string[k + l]:
                    issame = False

            if issame:
                twice = True

    if twice:
        ans = i + 1
    else:
        break

print(ans)
def unread_programmers(n, m, p, messages):
    # 모든 프로그래머들을 나타내는 집합을 생성
    all_programmers = set(chr(ord('A') + i) for i in range(n))
    
    # 메세지를 확인한 프로그래머들을 나타내는 집합
    read_programmers = set()

    # p번째 메세지 이전의 메세지를 확인하며 읽은 프로그래머들을 업데이트
    for i in range(p - 1):
        read_programmers.update(messages[i][0])

    # p번째 메세지 이후에 메세지를 보낸 프로그래머들을 읽은 프로그래머들에 추가
    for i in range(p - 1, m):
        read_programmers.update(messages[i][0])

    # 읽지 않은 프로그래머들을 찾아낸다
    unread_programmers = all_programmers - read_programmers

    # 결과를 사전순으로 정렬하여 출력
    result = sorted(list(unread_programmers))
    print(" ".join(result))

# 입력 예제
n, m, p = map(int, input().split())
messages = [input().split() for _ in range(m)]

# 함수 호출 및 결과 출력
if messages[p-1][1] == 0:
    print(" ")
else:
    unread_programmers(n, m, p, messages)
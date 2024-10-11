from collections import deque

# 입력 처리
N, M, Q = map(int, input().split())
people = input().split()

# M개의 줄을 만듦 (각 줄은 deque로 처리)
lines = [deque() for _ in range(M)]

# 각 사람을 해당 줄에 배치
for i, person in enumerate(people):
    line_idx = i % M
    lines[line_idx].append(person)

# 사람의 이름을 인덱스 찾기 쉽게 딕셔너리로 만듦
position = {person: i % M for i, person in enumerate(people)}

# 명령 처리
for _ in range(Q):
    command = input().split()
    
    if command[0] == '1':
        # 1 a b : a가 b 앞에 새치기
        a, b = command[1], command[2]
        line_idx = position[a]
        lines[line_idx].remove(a)  # a를 원래 위치에서 제거
        idx_b = lines[line_idx].index(b)  # b의 위치를 찾음
        lines[line_idx].insert(idx_b, a)  # b 앞에 a 삽입
    
    elif command[0] == '2':
        # 2 a : a가 집으로 감
        a = command[1]
        line_idx = position[a]
        lines[line_idx].remove(a)  # a를 줄에서 제거
    
    elif command[0] == '3':
        # 3 a b c : a부터 b까지 사람들을 떼어내어 c 앞으로 이동
        a, b, c = command[1], command[2], command[3]
        line_a_b = position[a]  # a와 b가 서 있는 줄
        line_c = position[c]    # c가 서 있는 줄
        
        # a부터 b까지의 사람들을 찾음
        idx_a = lines[line_a_b].index(a)
        idx_b = lines[line_a_b].index(b)
        group = deque()  # 떼어낼 그룹을 저장할 덱
        
        for i in range(idx_a, idx_b + 1):
            group.append(lines[line_a_b][i])
        
        # 원래 줄에서 a부터 b까지 제거
        for i in range(idx_b, idx_a - 1, -1):
            lines[line_a_b].remove(lines[line_a_b][i])
        
        # c 앞에 그룹을 삽입
        idx_c = lines[line_c].index(c)
        for person in reversed(group):
            lines[line_c].insert(idx_c, person)

# 결과 출력
for line in lines:
    if line:
        print(' '.join(line))
    else:
        print(-1)
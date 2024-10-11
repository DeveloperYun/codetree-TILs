from collections import deque

def process_lines(N, M, Q, names, commands):
    # 각 줄을 deque로 관리하여 효율적인 삽입/삭제 처리
    lines = [deque() for _ in range(M)]
    people_to_line = {}  # 사람의 이름을 줄 번호로 매핑
    
    # 초기 줄 배치
    X = N // M
    for i, name in enumerate(names):
        line_num = i // X
        lines[line_num].append(name)
        people_to_line[name] = line_num
    
    # 명령 처리
    for command in commands:
        parts = command.split()
        if parts[0] == '1':  # 1 a b : a가 b 앞으로 새치기
            a, b = parts[1], parts[2]
            # a와 b의 현재 위치 찾기
            a_line = people_to_line[a]
            b_line = people_to_line[b]
            
            if a_line == b_line:  # 같은 줄에 있으면 a를 먼저 제거 후, b 앞으로 삽입
                lines[a_line].remove(a)
                idx_b = lines[b_line].index(b)
                lines[b_line].insert(idx_b, a)
            else:
                lines[a_line].remove(a)
                idx_b = lines[b_line].index(b)
                lines[b_line].insert(idx_b, a)
                people_to_line[a] = b_line
        
        elif parts[0] == '2':  # 2 a : a가 집에 감
            a = parts[1]
            a_line = people_to_line[a]
            lines[a_line].remove(a)
            del people_to_line[a]
        
        elif parts[0] == '3':  # 3 a b c : a부터 b까지 통째로 c 앞에 새치기
            a, b, c = parts[1], parts[2], parts[3]
            a_line = people_to_line[a]
            c_line = people_to_line[c]
            
            idx_a = lines[a_line].index(a)
            idx_b = lines[a_line].index(b)
            group = [lines[a_line][i] for i in range(idx_a, idx_b + 1)]
            
            # a~b까지를 원래 줄에서 제거
            for person in group:
                lines[a_line].remove(person)
                people_to_line[person] = c_line
            
            # c 앞에 삽입
            idx_c = lines[c_line].index(c)
            for person in reversed(group):  # 그룹을 역순으로 삽입
                lines[c_line].insert(idx_c, person)
    
    # 최종 결과 출력
    result = []
    for line in lines:
        if line:
            result.append(' '.join(line))
        else:
            result.append("-1")
    
    return result

# 입력 처리
N, M, Q = map(int, input().split())
names = input().split()
commands = [input() for _ in range(Q)]

# 줄 상태 처리 및 결과 출력
result = process_lines(N, M, Q, names, commands)
for line in result:
    print(line)
from collections import deque

def process_lines(N, M, Q, names, commands):
    # 각 줄을 deque로 관리
    lines = [deque() for _ in range(M)]
    people_pos = {}  # 사람의 위치를 저장하는 딕셔너리 (줄 번호, 인덱스)
    
    # 초기 줄 배치
    X = N // M
    for i, name in enumerate(names):
        line_num = i // X
        lines[line_num].append(name)
        people_pos[name] = (line_num, len(lines[line_num]) - 1)
    
    # 명령 처리
    for command in commands:
        parts = command.split()
        if parts[0] == '1':  # 1 a b : a가 b 앞으로 새치기
            a, b = parts[1], parts[2]
            a_line, _ = people_pos[a]
            b_line, b_idx = people_pos[b]
            
            # a가 있는 줄에서 제거
            lines[a_line].remove(a)
            
            # b가 있는 줄에서 a를 삽입
            lines[b_line].insert(b_idx, a)
            
            # 위치 정보 업데이트
            people_pos[a] = (b_line, b_idx)
            # b 이후 사람들의 인덱스도 업데이트
            for i in range(b_idx + 1, len(lines[b_line])):
                person = lines[b_line][i]
                people_pos[person] = (b_line, i)
        
        elif parts[0] == '2':  # 2 a : a가 집에 감
            a = parts[1]
            a_line, a_idx = people_pos[a]
            # 줄에서 제거
            lines[a_line].remove(a)
            del people_pos[a]
            # 제거 이후 사람들의 인덱스 업데이트
            for i in range(a_idx, len(lines[a_line])):
                person = lines[a_line][i]
                people_pos[person] = (a_line, i)
        
        elif parts[0] == '3':  # 3 a b c : a부터 b까지 통째로 c 앞으로 새치기
            a, b, c = parts[1], parts[2], parts[3]
            a_line, a_idx = people_pos[a]
            b_line, b_idx = people_pos[b]
            c_line, c_idx = people_pos[c]
            
            # a부터 b까지의 그룹 추출
            group = [lines[a_line][i] for i in range(a_idx, b_idx + 1)]
            
            # a부터 b까지 제거
            for person in group:
                lines[a_line].remove(person)
                del people_pos[person]
            
            # c 앞으로 삽입
            for i, person in enumerate(group):
                lines[c_line].insert(c_idx + i, person)
                people_pos[person] = (c_line, c_idx + i)
            
            # c 이후 사람들의 인덱스 업데이트
            for i in range(c_idx + len(group), len(lines[c_line])):
                person = lines[c_line][i]
                people_pos[person] = (c_line, i)
    
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
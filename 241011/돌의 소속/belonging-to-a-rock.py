def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    Q = int(data[1])
    
    # 그룹 정보를 저장할 배열
    group = [0] * (N + 1)
    
    # 누적 합 배열 초기화
    count1 = [0] * (N + 1)
    count2 = [0] * (N + 1)
    count3 = [0] * (N + 1)
    
    # 각 돌의 그룹 입력 받기
    for i in range(1, N + 1):
        group[i] = int(data[i + 1])
    
    # 누적 합 계산
    for i in range(1, N + 1):
        count1[i] = count1[i - 1]
        count2[i] = count2[i - 1]
        count3[i] = count3[i - 1]
        
        if group[i] == 1:
            count1[i] += 1
        elif group[i] == 2:
            count2[i] += 1
        elif group[i] == 3:
            count3[i] += 1
            
    # 쿼리 처리
    output = []
    query_start_index = N + 2
    for i in range(Q):
        a = int(data[query_start_index + i * 2])
        b = int(data[query_start_index + i * 2 + 1])
        
        cnt1 = count1[b] - count1[a - 1]
        cnt2 = count2[b] - count2[a - 1]
        cnt3 = count3[b] - count3[a - 1]
        
        output.append(f"{cnt1} {cnt2} {cnt3}")
    
    # 결과 출력
    print("\n".join(output))

if __name__ == "__main__":
    main()
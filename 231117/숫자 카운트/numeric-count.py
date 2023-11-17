n = int(input())
nums = []
for _ in range(n):
    n, c1, c2 = map(int, input().split())
    n = list(map(int, str(n)))
    # [첫째자리수, 둘째자리수, 셋째자리수, 카운트1, 카운트2] 형태로 입력 시켜놓는다.
    nums.append([n[0], n[1], n[2], c1, c2])

a_arr = [] # i j k가 반복하면서 만든 값들을 담아주기 위한 배열

cnt = 0
# for i in range(1, 10) :
#     for j in range(10) :
#         for k in range(10) :
#             if i == j or j == k or i == k :
#                 continue
#             for n in nums :
#                 print(n)
#                 cnt1 = 0
#                 cnt2 = 0
#                 for q in range(3) :
#                     if n[q] == i or n[q] == j or n[q] == k :
#                         cnt1 += 1 
#                     elif (i in n and n[q] != i) or (j in n and n[q] != j) or (k in n and n[q] != k) :
#                         cnt2 += 1
#                 if cnt1 == n[3] or cnt2 == n[4] :
#                     cnt += 1

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k : # 서로 다른 수라는 조건 때문에 필터링
                continue

            satisfied = True # (i, j, k)쌍에 대해 밑에 조건을 다 만족시킬 수 있다면 True / 그렇지 않다면 False
            for n in nums :
                #print(n)
                cnt1 = 0
                cnt2 = 0
                #for _ in range(3) :
                m = [i, j, k]

                for l in range(3):
                    for q in range(3):
                        if n[l] == m[q]:
                            if l == q:
                                cnt1 += 1
                            else:
                                cnt2 += 1
                
                if cnt1 != n[3] or cnt2 != n[4] :
                    satisfied = False
                    #break
            
            # 전부 살펴봤음에도 다 만족한다면 답을 갱신합니다.
            if satisfied == True:
                cnt += 1
print(cnt)
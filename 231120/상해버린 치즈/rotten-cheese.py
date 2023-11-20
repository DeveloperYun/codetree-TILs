N, M, D, S = tuple(map(int, input().split()))
# (p번째 사람, m번째 치즈, t초) 먹음
eaten = list(tuple(map(int, input().split())) for _ in range(D))
# (p번째 사람, t초) 아픔
bad_condition = list(tuple(map(int, input().split())) for _ in range(S))

# Step1 : 상한 치즈 고르기
gone_cheezes = [[] for _ in range(N+1)]

bad_dict = {}
for bad in bad_condition :
    p, t = bad
    bad_dict[p] = t

eaten_dict = {}
## 아프기 전 섭취했다면 ? 주워담는다.
for eat in eaten :
    p, m, t = eat
    if eaten_dict.get(p):
        eaten_dict[p].append((t, m))
    else :
        eaten_dict[p] = [(t, m)]

for bad_p, bad_t in bad_dict.items()  :
    # print(bad_p, bad_t)
    # bad_t 이하로, bad_p의 치즈를 gone_cheezes[bad_p]에 주워담는다.
    for eat_p, eat_cheezes in eaten_dict.items():
        # print(eat_p, eat_cheezes)
        for eat_t, eat_cheeze in eat_cheezes :
            if eat_t < bad_t and eat_p == bad_p :
                gone_cheezes[bad_p].append(eat_cheeze)

### 주워담은 것들을 교집합 해서 상한 후보를 구한다.

gone_cheezes = [i for i in gone_cheezes if i] # 유효값
if gone_cheezes :
    candi = list(set(gone_cheezes[0]).intersection(*gone_cheezes[1:]))


# Step2 : 먹은 사람 세기
max_cnt = 0
for i in candi :
    cnt = 0
    for eat_p, eat_cheezes in eaten_dict.items():
        for _, num in eat_cheezes :

            if i == num :
                cnt += 1
                break
                
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
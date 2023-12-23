# 변수 선언 및 입력:
n = int(input())

# 입력받은 학생 이름과 점수 변동값을 저장합니다.
changes = [
    input().split()
    for _ in range(n)
]

def get_status(score1, score2, score3):
    # 1. A만 명예의 전당에 올라가 있는 경우
    if score1 > score2 and score1 > score3:
        return 1
    # 2. B만 명예의 전당에 올라가 있는 경우
    elif (score2 > score1) and (score2 > score3):
        return 2
    # 3. C만 전당에 올라가 있는 경우 
    elif score3 > score1 and score3 > score2:
        return 3
    # 4. A,B만 올라가있는 경우
    elif score1 == score2 and score1 != score3:
        return 4
    elif score2 == score3 and score2 != score1:
        return 5
    elif score1 == score3 and score1 != score2:
        return 6
    # 3. A, B 둘 다 명예의 전당에 올라가 있는 경우
    else:
        return 7


# 현재 A, B의 점수를 나타냅니다.
score_a, score_b, score_c = 0, 0, 0
ans=0
for name, value in changes:
    value = int(value)

    if name == "A":
        if get_status(score_a,score_b,score_c) != get_status(score_a+value,score_b,score_c):
            ans += 1
        
        score_a += value
    
    elif name=="B":
        if get_status(score_a,score_b,score_c) != get_status(score_a,score_b+value,score_c):
            ans += 1
        
        score_b += value

    else:
        if get_status(score_a,score_b,score_c) != get_status(score_a,score_b,score_c+value):
            ans += 1
        
        score_c += value

print(ans)
def count_hall_of_fame_changes(n, changes):
    hall_of_fame_changes = 0
    scores = {'A': 0, 'B': 0}
    hall_of_fame = set()

    for i in range(n):
        player, score_change = changes[i]
        scores[player] += score_change

        max_score = max(scores.values())

        new_hall_of_fame = {player for player, score in scores.items() if score == max_score}

        if new_hall_of_fame != hall_of_fame:
            hall_of_fame_changes += 1
            hall_of_fame = new_hall_of_fame

    return hall_of_fame_changes


# 입력 받기
n = int(input())
changes = [input().split() for _ in range(n)]
changes = [(player, int(score)) for player, score in changes]

# 결과 출력
if n==1:
    print(0)
else:
    result = count_hall_of_fame_changes(n, changes)
    print(result)
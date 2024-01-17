def get_consecutive_counts(maps):
    n = len(maps)
    consecutive_counts = [0] * n
    count = 0
    for i in range(n-1, 0, -1):
        if maps[i] == maps[i-1]:
            count += 1
        else:
            count = 0
        consecutive_counts[i] = count
    return consecutive_counts


def can_bomb(consecutive_counts, m):
    return any(count >= m-1 for count in consecutive_counts)


def bomb(maps, consecutive_counts, m):
    if m == 1:
        return []
    n = len(maps)
    bombed = [0] * n
    for i, count in enumerate(consecutive_counts):
        if count >= m-1:
            for j in range(i-1, i+count):
                bombed[j] = 1
    return [maps[i] for i in range(n) if not bombed[i]]


n, m = map(int, input().split())
maps = [int(input()) for _ in range(n)]

while True:
    consecutive_counts = get_consecutive_counts(maps)
    if not can_bomb(consecutive_counts, m):
        break
    maps = bomb(maps, consecutive_counts, m)

print(len(maps))
for value in maps:
    print(value)
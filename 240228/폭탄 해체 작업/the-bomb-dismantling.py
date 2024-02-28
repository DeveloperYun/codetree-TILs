from heapq import heappush, heappop

t = int(input())
bombs = [list(map(int, input().split())) for _ in range(t)]
bombs.sort(key= lambda x: (x[1], x[0]))
MAX_TIME = bombs[-1][-1]

bomb_list = [[] for _ in range(MAX_TIME + 1)]
for score, limit in bombs:
    bomb_list[limit].append(score)

heap = []
cnt = 0
for time in range(MAX_TIME, 0, -1):
    for score in bomb_list[time]:
        heappush(heap, -score)
    if len(heap) == 0:
        continue
    q = -heappop(heap)
    cnt += q
    
print(cnt)
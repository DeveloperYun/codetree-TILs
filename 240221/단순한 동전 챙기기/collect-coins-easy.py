n=int(input())
answer = 2000

grid=[
    list(map(str,input().rstrip()))
    for _ in range(n)
]

# s에서 출발해서 최소 3개의 동전을 수집해서 E로 도착.
# 동전은 번호 증가 순서대로 수집
# 같은 위치 방문 가능 
# 최소 이동 횟수를 구하라.

start_x, start_y = 0, 0
end_x, end_y = 0, 0
coins=[] #값
coins_coord = {} #{동전번호 : (x,y)}
for x in range(n):
    for y in range(n):
        if grid[x][y] == 'S':
            start_x,start_y = x,y
        if grid[x][y] == 'E':
            end_x,end_y = x,y
        if '1' <=grid[x][y] <='9':
            num = int(grid[x][y])
            coins.append(num)
            coins_coord[num] = (x,y)

coins.sort() #번호 순서대로 뽑아야하므로 정렬
coin_count = len(coins)

def dist(a,b):
    x1, y1 = a
    x2, y2 = b

    return abs(x1-x2) + abs(y1-y2)

for i in range(coin_count):
    for j in range(i+1,coin_count):
        for k in range(j+1,coin_count):
            move = 0

            #세 점의 좌표 
            p1 = coins_coord[coins[i]]
            p2 = coins_coord[coins[j]]
            p3 = coins_coord[coins[k]]
            coords = [(start_x,start_y),p1,p2,p3,(end_x,end_y)]

            for idx in range(4):
                move += dist(coords[idx],coords[idx+1])

            answer = min(answer,move)

if answer == 2000:
    print(-1)
else:
    print(answer)
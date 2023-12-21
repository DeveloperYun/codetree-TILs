from sys import stdin
x = int(stdin.readline())

#최대 속도로 간 후 유지하다가 내려가는 게 가장 빠를 것!
#k가 최대 속도라면 유지한 것은 k이하의 속도가 가능!

speed = 0
idx = 0
cnt = 0
while idx + 2*(speed+1) <= x: #올라가고 내려감으로 최고 속도 계산
    speed += 1
    idx += 2*speed
    cnt += 2
    print("중간체크", idx, cnt, speed)

if idx + speed + 1 < x: #최고 속도가 1번시
    idx += speed + 1
    cnt += 1
    speed += 1
    print("최고 속도 한번", idx, cnt, speed)

#하지만 (1)이든 (2)를 주석처리 해도 되는 이유는 speed가 1씩 증가해 speed*2가 항상 speed+1보다 크기 때문이다.
#따라서 유지하는 경우는 한 번만 나온다.

#아래의 while문을 //문으로 변경
#최고 속도 아래의 값은 언제든 유지하면 됨
#-(1)
# while idx <= x-speed:
#     idx += speed
#     cnt += 1    
# print(idx, cnt, speed)
# print(cnt if idx == x else cnt + 1)

#-(2)
# tmp = (x - idx)//speed
# cnt += tmp
# idx += speed*tmp
# print(idx, cnt, speed)


print(cnt if idx == x else cnt + 1) #idx가 x가 아니면 speed이하에서 한번 유지시켜야함
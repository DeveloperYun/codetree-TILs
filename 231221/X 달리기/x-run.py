n = int(input())

dist = 0
time = 0
speed = 0

# 중간 지점까지 속도 상승
for i in range(1, n+1):
    dist += i
    time += 1
    if dist >= n // 2:
        speed = i
        break

while dist < n:
    if (speed * (speed+1))/2 > n - dist:
        speed -= 1
    dist += speed
    time += 1

print(time)
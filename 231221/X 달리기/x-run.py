def shortest_time_to_destination(X):
    time = 0
    position = 0
    speed = 1

    while position < X:
        time += 1
        position += speed
        if position >= X:
            break
        time += 1
        position += speed
        speed += 1

    return time

# 입력 받기
X = int(input())

# 결과 출력
print(shortest_time_to_destination(X))
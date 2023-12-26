n = int(input())

location_list = [0] * 2001

location = 1000 #현재위치 1000
for i in range(n):
    x, direction = input().split()
    x = int(x)

    if direction == "L":
        for i in range(location-x, location):
            location_list[i] +=1
        location -= x
    else:
        for i in range(location, location+x):
            location_list[i] +=1
        location += x

cnt = 0 
for j in location_list:
    if j >= 2:
        cnt+=1
print(cnt)
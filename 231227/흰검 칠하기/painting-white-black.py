n=int(input())
arr=[0]*2000001

segments=[]
#현재 위치
cur=0

for _ in range(n):
    dist, direction = map(str,input().split())
    dist = int(dist)

    if direction == "R":
        #오른쪽으로 이동할 경우 : cur ~ cur + distance 이동
        section_left = cur
        section_right = cur + dist
        cur += dist
    else:
        #go left : cur - dist ~ cur
        section_left = cur - dist
        section_right = cur
        cur -= dist

    segments.append([section_left,section_right,direction])

offset = 100000
for x1,x2,direction in segments:
    #offset을 더해줘야한다.
    x1 += offset
    x2 += offset
    temp=[]
    #구간 색칠
    if direction=="R":
        for i in range(x1,x2):
            if arr[i] != 0:
                arr[i].append('black')
            else:
                arr[i] = ['black']
    else:
        for i in range(x1,x2):
            if arr[i] != 0:
                arr[i].append('white')
            else:
                arr[i] = ['white']

white,black,gray=0,0,0
for a in arr:
    if a != 0:
        if a.count('black') >= 2 and a.count('white') >= 2:
            gray += 1
        else:
            if a[-1] == "black":
                black += 1
            else:
                white += 1

print(white,black,gray)
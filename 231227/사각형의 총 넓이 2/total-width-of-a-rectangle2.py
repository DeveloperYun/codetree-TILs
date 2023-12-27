n=int(input())
x1,y1,x2,y2=map(int,input().split())
a1,b1,a2,b2=map(int,input().split())

max_x = max(x1,x2,a1,a2)
max_y = max(y1,y2,b1,b2)

max_x += 1
max_y += 2

arr=[]
for _ in range(max_y):
    temp = [0]*max_x
    arr.append(temp)

for i in range(x1,x2):
    for j in range(y1,y2):
        arr[i][j] = 1

for i in range(a1,a2):
    for j in range(b1,b2):
        arr[i][j] = 1
        
cnt=0
for i in range(max_x):
    for j in range(max_y):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)
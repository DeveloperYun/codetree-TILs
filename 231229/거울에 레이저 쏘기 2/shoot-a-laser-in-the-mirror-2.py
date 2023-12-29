def dir_code23(inputLight): #23은 / 을 2번 3번꼭지점으로 생각하여 분류한 것 입니다.
    if inputLight == 0: # 들어가는 방향
        return 1        # 나가는방향이면서 다음 번 거울이 받는 방향
    elif inputLight == 1:
        return 0
    elif inputLight == 2:
        return 3
    else:
        return 2
def dir_code14(inputLight):
    if inputLight == 0:
        return 3
    elif inputLight == 3:
        return 0
    elif inputLight == 1:
        return 2
    else:
        return 1

def move(dir_now): # 반사돼 나오는 빛의 이동경로를 표시한 함수입니다.
    if dir_now == 0:
        return [1 ,0]
    elif dir_now == 1:
        return [0 ,-1]
    elif dir_now == 2:
        return [-1,0]
    else:
        return [0,1]



n = int(input())

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

array = [[0 for i in range(n)] for j in range(n)]      #거울이 들어있는 배열
arrayLight = [[0 for i in range(n)] for j in range(n)] #반사된 빛이 들어있는 배열
lightstep = 0 #빛이 몇번 반사됐는지 나타냅니다.

for i in range(n):
    mirror = input()
    for j in range(n):
        array[i][j] = mirror[j]

inLight = int(input())-1

start_dir = inLight // n  # 들어갈 방향
start_num = inLight % n  # 들어갈 방향에서의 번호

x , y = 0, 0   # 가로 세로

if start_dir == 0: # 위에서 진입할때
    x = 0
    y = start_num 
elif start_dir == 1: # 오른쪽에서 진입할때
    x = start_num 
    y = n - 1
elif start_dir == 2: # 아래에서 진입할때
    x = n - 1
    y = n - start_num -1
else:
    x = n - start_num -1 #왼쪽에서 진입할때
    y = 0

dir_now = start_dir 

while True:
    #일단 들어가면서 불을 킨다
    lightstep += 1
    arrayLight[x][y] = lightstep

    if array[x][y] == "/":
        dir_now = dir_code23(dir_now)
        dx , dy = move(dir_now)
        x += dx
        y += dy
        #print(dir_now,x , y )
    else:
        dir_now = dir_code14(dir_now)
        dx , dy = move(dir_now)
        x += dx
        y += dy
        #print(dir_now,x , y )
    
    if in_range(x, y)!=True: #만약 빛이 범위 밖으로 빠져나왔다면 출력해줍니다.
        #print("Break {0} {1}".format(x,y))
        break

print(lightstep)
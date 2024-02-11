n,m,t,k = map(int,input().split())
marbles = []

mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

def in_range(x,y):
    return 0<=x<n and 0<=y<n 

for i in range(m):
    r,c,d,v = map(str,input().split())
    r,c,v = int(r)-1,int(c)-1,int(v)
    marbles.append((r,c,mapper[d],v,i+1)) #마지막 i는 구슬의 번호를 나타낸다. 
    # r행, c열, d방향으로 속도 v로 이동 중.

def move(marble):
    #벽에 부딪혔을 때 반대방향으로 가야하므로 아래와 같이 dx,dy를 설정한다.
    dx = [-1,0,0,1]
    dy = [0,1,-1,0]

    x,y,move_dir,velocity,marble_num = marble
    
    for i in range(velocity):
        #바로 앞에 벽이 있는지 확인한다.
        nx = x + dx[move_dir]
        ny = y + dy[move_dir]

        #벽이 없는 경우라면 그대로 velocity 만큼 이동
        if in_range(nx,ny):
            x, y = nx, ny
        
        #벽이 있는 경우라면 방향을 반대로 적용한 것을 고려해서 velocity 만큼 이동
        else: 
            move_dir = 3-move_dir
            x = x + dx[move_dir]
            y = y + dy[move_dir]

    return (x,y,move_dir,velocity,marble_num)

def move_all():
    for i, marble in enumerate(marbles):
        marbles[i] = move(marble) #각 구슬이 움직이고난 뒤에 위치 정보를 갱신한다.
    
def remove_duplicate_marbles():
    global marbles

    #우선순위
    # 1. 구슬의 속도 => 2. 구슬의 번호 
    # 속도 : 3번째 항, 번호 : 4번째 항(마지막 항)
    #단, k개가 넘는 경우에만 제거한다. 
    marbles.sort(key=lambda x: (x[3],x[4]), reverse=True)
   
    #이제 marbles 에서 k개 이상 겹치는 게 있는지 확인하면 된다. 
    temp = []
    for i in range(len(marbles)):
        if i >= len(marbles):
            break
        temp.append(marbles[i])
        for j in range(i+1,len(marbles)):
            #같은 좌표라면 
            if marbles[i][0] == marbles[j][0] and marbles[i][1] == marbles[j][1]:
                temp.append(marbles[j])
        #만약 temp 길이가 1이라면, 같은 좌표가 없다는 뜻이므로 temp를 reset
        if len(temp) == 1:
            temp = []
        
        #temp 길이가 k를 넘으면 k개 까지만 살아남아야한다.
        if len(temp) > k :
            #현재 temp에는 k개 초과의, 중복되는 구슬 정보가 들어있다.
            dont_remove_info = []
            for z in range(k):
                dont_remove_info.append(temp[z])

            remove_info = []
            for zz in range(len(temp)):
                if temp[zz] not in dont_remove_info:
                    remove_info.append(temp[zz])

            #marbles에서 remove_info를 뺀다.
            newmarbles=[]
            for q in range(len(marbles)):
                if marbles[q] not in remove_info:
                    newmarbles.append(marbles[q])
            
            marbles = newmarbles
            temp = []
        else:
            temp = []
def simulate():
    #step1
    #구슬을 일단 한 번씩 움직여본다.
    #이 때, 구슬은 각 속도만큼 움직인다.
    move_all()

    #step2
    #움직임 이후에 겹치는 것을 우선순위에 따라 지워준다.
    remove_duplicate_marbles()

#t초가 지난 이후에 살아남은 구슬의 개수를 구해야하므로
for _ in range(t):
    simulate()
    
print(len(marbles))
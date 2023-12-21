x=int(input())
answer=0
for i in range(1,10001):
    #i = 속도가 감소하기 시작하는 위치
    val=0
    for j in range(0,i):
        val += 1
    
    for k in range(i,x):
        val -= 1
        if k==(x-1) and val==0:
            print(i+1)
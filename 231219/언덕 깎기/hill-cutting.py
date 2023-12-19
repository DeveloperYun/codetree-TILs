n=int(input())
arr=[
    int(input()) for _ in range(n)
]

def check(l,r):
    cnt = 0
    for elem in arr:
        if elem < l or elem > r:
            cnt += min(abs((l-elem)**2), abs((elem-r)**2))
    
    return cnt


answer=9999999
MAXNUM = 1000

for i in range(1,MAXNUM+1):
    #구간 [i,i+17] 사이에 들어있는 숫자를 센다
    #예를 들어 1~17 사이에 있어야 한다 가정하면 그떄 드는 비용을 반환받는다
    answer = min(answer, check(i,i+17))

print(answer)
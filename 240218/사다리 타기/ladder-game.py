from itertools import combinations
import sys

n,m=map(int,input().split())

horizontal = [] #가로줄의 상태 
result = [x for x in range(1,n+1)] #최종 결과 
for _ in range(m):
    # 해당 가로줄은 왼쪽에서부터 a번째 세로줄과 a+1번째 세로줄을 연결하며, 위에서부터 b번째 위치에 가로줄이 그어짐을 나타냅니다.
    a,b=map(int,input().split())
    horizontal.append((a,b))

horizontal.sort(key=lambda x:x[1]) # [(1, 1), (2, 2), (1, 3), (3, 3), (2, 4), (3, 5)]

for hor in horizontal:
    #hor = (1,1)
    x,y = hor

    result[x-1], result[x] = result[x], result[x-1]

#가로 줄이 15개 밖에 안되는데 그냥 조합을 쓸까? 
#1개만 썼을 때부터 m개를 썼을때로 확인해나간다면?
def check(select):
    test = [x for x in range(1,n+1)]

    for sec in select:
        x,y=sec
        test[x-1],test[x] = test[x],test[x-1]
    
    if test == result:
        return True
    
    return False

find = 0
for i in range(1,m+1):

    temp = list(combinations(horizontal,i))
    '''
    [((1, 1), (2, 2)), 
    ((1, 1), (1, 3)), 
    ((1, 1), (3, 3)), 
            ...
    ((2, 4), (3, 5))]
    '''
    for t in temp:
        #t = (1,1), (2,2)
        if check(t):
            if i==n:
                print(0)
            else:
                print(i)
            sys.exit(0)
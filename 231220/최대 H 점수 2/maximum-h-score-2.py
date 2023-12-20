from itertools import combinations
import copy

n,l = map(int,input().split()) 
arr=list(map(int,input().split()))
data = []
'''
L만큼 nCl 을 통해서 1씩 올릴 원소를 고르는 모든 경우의
수를 temp에 담아서 최대 H 값을 갱신한다.
'''
for idx,val in enumerate(arr):
    data.append((idx,val))

def get_h(array):
    cnt = 0
    #array = [2,3,5]
    for i in array:
        h = 0
        for j in array:
            if j >= i:
                h+=1
        if h>=i:
            cnt = max(cnt, i)
    
    return cnt

answer = 0
#l=0인 경우는 예외처리한다.
if l==0:
    answer=max(answer,get_h(arr))
    print(answer)
else:
    temp=list(combinations(data,l))
    for d in temp:
        #d = ((0, 1), (1, 100))

        temp = copy.deepcopy(arr)
        for i in d:
            #i = (0,1)
            #arr의 i[0] 번째 값을 1 더해준다.
            
            temp[i[0]] = temp[i[0]] + 1
        
        #이제 temp에 대해서 h값 구하면 된다.
        answer = max(answer,get_h(temp))
    print(answer)
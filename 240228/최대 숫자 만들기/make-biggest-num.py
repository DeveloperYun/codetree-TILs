from functools import cmp_to_key

n=int(input())
arr=[]
for _ in range(n):
    x=str(input())
    arr.append(x)

#첫째 자리, 둘째자리, 셋째 자리...순으로 reverse 정렬해야한다
#만약 없는 경우에는 없는게 우선순위다(ex. 8 > 83)

def compare(x, y):
    # 비교 함수
    if len(x)==len(y):
        if int(y)>int(x):
            return 1
    
    if len(x) != len(y) and y[0] == x[0]:
        return 1

    if x > y:
        return -1
    
    if y > x:
        return 1

    return 0

arr.sort(key=cmp_to_key(compare))
print(''.join(arr))
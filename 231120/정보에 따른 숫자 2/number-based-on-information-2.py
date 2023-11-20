t,a,b=map(int,input().split())

s_arr=[]
n_arr=[]
for i in range(t):
    c,x = map(str,input().split())
    x=int(x)
    if c=="S":
        s_arr.append(x)
    elif c=="N":
        n_arr.append(x)

s_arr.sort() #1, 10
n_arr.sort() #4

def solution(target):
    #i랑 가장 가까운 s까지의 거리 d1
    len_s = len(s_arr)
    len_n = len(n_arr)
    ts=[]
    tn=[]
    for i in range(len_s):
        ts.append(abs(target-s_arr[i]))
    
    for i in range(len_n):
        tn.append(abs(target-n_arr[i]))
    
    ts.sort()
    tn.sort()

    d1 = ts[0]
    d2 = tn[0]

    if d1 <= d2:
        return True
    else:
        return False

cnt=0
for i in range(a,b+1):
    #숫자 i에 대해서 탐색 시작
    if solution(i):
        cnt += 1

print(cnt)
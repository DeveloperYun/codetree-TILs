n,k=map(int,input().split())
arr = list(map(int,input().split()))
#2,3,5,4,1 

def is_possible(a):
    available = []
    # a = 4
    for i, elem in enumerate(arr):
        if elem <= a:
            available.append(i)
    
    arsize = len(available)
    for i in range(1,arsize):
        dist = available[i] - available[i-1]
        if dist > k:
            return False
    
    return True

answer=9999999

for a in range(max(arr[0],arr[-1]), n+1):
    if is_possible(a):
        answer = min(answer,a)

if k==1:
    print(max(arr))
else:
    print(answer)
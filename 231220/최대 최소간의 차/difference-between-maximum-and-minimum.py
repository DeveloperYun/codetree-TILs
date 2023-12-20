n,k=map(int,input().split())
arr=list(map(int,input().split()))

maxnum=10000

'''
답이 i~i+k 라고 하고 이 때 드는 비용을 계산해서 min을 구한다.
'''
answer = 9999999
for i in range(1,maxnum+1):
    cnt = 0
    for j in range(n):
        if arr[j] < i:
            change = abs(arr[j]-i)
        elif arr[j] > i+k:
            change = abs(arr[j] - (i+k))
        else:
            change = 0
    
        cnt += change
    answer = min(answer,cnt)
print(answer)
import copy

n=int(input())
arr=[]
for i in range(n):
    a,b,c=map(int,input().split())
    arr.append([a,b,c])

#a,b를 swap 하고 c를 열어본다.

answer=0

# n번 수행한다.

for i in range(1,4):
    # i번에 조약돌이 있다고 가정하면
    temp = [0]*4
    temp[i] = 1
    cnt=0
    for a,b,c in arr:
        temp[a],temp[b]=temp[b],temp[a]

        if temp[c]==1:
            cnt+=1
    
    answer = max(answer,cnt)
print(answer)
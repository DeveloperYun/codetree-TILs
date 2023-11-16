import sys
n=int(input())

arr=[]
for i in range(n):
    pos, alpha = map(str,input().split())
    pos = int(pos)
    arr.append((pos,alpha))

arr.sort()

answer = 0 #9..9
a1,a2=-1,-1
for i in range(n):
    for j in range(i+1,n):
        countG, countH = 0,0

        for k in range(i,j+1):
            
            if arr[k][1]=='H':
                countH += 1
            elif arr[k][1]=='G':
                countG += 1
        
        if  countH==0 or countG==0 or countH == countG:
            length = arr[j][0]-arr[i][0]
            answer = max(answer,length)

print(answer)
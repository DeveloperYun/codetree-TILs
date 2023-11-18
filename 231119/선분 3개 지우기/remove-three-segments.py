n=int(input())
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))
answer=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if i==j or i==k or j==k:
                continue

            #i, j, k 선분을 제외
            temp = [0]*100 
            flag = True

            for x in range(n):
                if x==i or x==j or x==k:
                    continue
                
                for y in range(arr[x][0],arr[x][1]+1):
                    temp[y] += 1
                    if temp[y] > 1:
                        flag = False
            
            if flag:
                answer += 1
print(answer)
import copy
n,b=map(int,input().split())
arr=[]
for i in range(n):
    p,s=map(int,input().split())
    arr.append([p,s])

answer=0

#한명의 학생에게 선물 쿠폰 쓸 때
for i in range(n):
    temp = copy.deepcopy(arr)
    temp[i][0] //= 2 #반값


    temp.sort(key=lambda x:(x[0]+x[1]))

    student = 0
    cnt=0

    for j in range(n):
        if cnt + temp[j][0] + temp[j][1] > b:
            break

        cnt += temp[j][0] + temp[j][1]
        student += 1
    
    answer = max(answer,student)
print(answer)
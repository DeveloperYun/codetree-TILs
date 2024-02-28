from functools import cmp_to_key

n=int(input())
arr=[]
for _ in range(n):
    x=int(input())
    arr.append(x)

answer=''
answer += str(arr[0]) #53
arr.pop(0)

while arr:
    x1 = arr.pop(0)
    
    t1 = answer + str(x1)
    t2 = str(x1) + answer

    if t1>t2:
        answer = t1
    else:
        answer = t2

print(answer)
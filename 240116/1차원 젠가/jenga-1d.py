n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)

s1,e1=map(int,input().split())
s2,e2=map(int,input().split())

temp = []
for i in range(0,s1-1):
    temp.append(arr[i])

for i in range(e1,n):
    temp.append(arr[i])

answer = []
for i in range(s2-1):
    answer.append(temp[i])
for i in range(e2,len(temp)):
    answer.append(temp[i])

print(len(answer))
for i in answer:
    print(i)
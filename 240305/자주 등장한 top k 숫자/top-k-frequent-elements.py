n,k=map(int,input().split())
arr=list(map(int,input().split()))

dic={}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

#value 내림차순 정렬을 해야한다. 
d = sorted(dic.items(), key=lambda x:(x[1],x[0]), reverse=True)


for i in range(k):
    print(d[i][0],end=' ')
n=int(input())
arr=[]
for _ in range(n):
    x,y=map(int,input().split())
    arr.append([x,y])

ans=[]


for i in range(101):
    for j in range(101):
        #x,y축에 평행한 각 선을 기준으로 4등분
        one,two,three,four=0,0,0,0
        for point in arr:
            x = point[0]
            y = point[1]
            if 0<x<i and 0<y<j:
                one += 1
            elif x>i and 0<y<j:
                two += 1
            elif x>i and y>j:
                three += 1
            else:
                four +=1
        s=[]
        s.append(one)
        s.append(two)
        s.append(three)
        s.append(four)
        ans.append(max(s))
    
print(min(ans))
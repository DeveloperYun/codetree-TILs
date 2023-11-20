x,y=map(int,input().split())

cnt=0

for i in range(x,y+1):
    temp = str(i)
    
    if temp == temp[::-1]:
        cnt += 1

print(cnt)
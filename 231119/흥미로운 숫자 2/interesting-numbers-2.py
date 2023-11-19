x,y=map(int,input().split())

cnt=0

def funny(n):
    temp = list(map(int,str(n)))
    
    #전부 같은 경우
    t=temp[0]
    if temp.count(t) == len(temp):
        return False
    
    #한 자리 이상 다른 경우
    #다른거 두개 찾아서 count 때리면 되나?
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            if temp[i] != temp[j]:
                c1 = temp.count(temp[i]) #1
                c2 = temp.count(temp[j]) #3

                #11 3
                if c1 > 1 and c2 == 1:
                    return True
                elif c1 == 1 and c2 > 1:
                    return True
                else:
                    return False
    return True
for i in range(x,y+1):
    if funny(i):
        cnt+=1

print(cnt)
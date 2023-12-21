n,m,p=map(int,input().split())

data=[]
member=[]
for _ in range(m): #m=메시지의 개수
    c, u = map(str,input().split()) #사람C가 올린 메세지, 아직 메시지를 읽지 않은 사람 수 U
    u = int(u)
    data.append((c,u))

answer=n
exp=[]
exp.append(data[p-1][0])
for i in range(p,n):
    if data[i][0] not in exp:
        exp.append(data[i][0])

for i in range(n):
    mem = chr(65+i)
    member.append(mem)

def subtract_lists(a, b):
    return [item for item in a if item not in b]

if data[p-1][1]==0:
    print(" ")
else:
    r = subtract_lists(member,exp)
    for i in r:
        print(i,end=" ")
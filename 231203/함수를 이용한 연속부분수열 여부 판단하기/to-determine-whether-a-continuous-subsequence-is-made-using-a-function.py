a,b=map(int,input().split())

lista=list(map(str,input().split())) # 2 4 6 8 5 7
listb=list(map(str,input().split())) # 4 6 8


aa = ''.join(lista)
bb = ''.join(listb)

if bb in aa:
    print("Yes")
else:
    print("No")
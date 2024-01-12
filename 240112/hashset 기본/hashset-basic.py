n=int(input())
s=set()

for i in range(n):
    a,b=map(str,input().split())
    b=int(b)

    if a=="add":
        s.add(b)
    elif a=="remove":
        s.remove(b)
    elif a=="find":
        if b in s:
            print('true')
        else:
            print('false')
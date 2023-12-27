n=int(input())
arr=[0]*2000001

w,b=0,0
cur = 100000
for _ in range(n):
    x,c=tuple(input().split())
    x=int(x)

    if c=="L":
        for i in range(cur-1,cur-x-1,-1):
            arr[i] = "white"
        
        cur -= x
    else:
        for i in range(cur,cur+x):
            arr[i] = "black"
        
        cur += x

print(arr.count("white"),arr.count("black"))
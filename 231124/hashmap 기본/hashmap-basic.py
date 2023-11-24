d = dict()

n=int(input())
for _ in range(n):
    x=tuple(map(str,input().split()))
    
    if x[0] == "add":
        d[x[1]] = x[2]
    elif x[0] == "find":
        if x[1] in d:
            print(d[x[1]])
        else:
            print("None")
    elif x[0] == "remove":
        d.pop(x[1])
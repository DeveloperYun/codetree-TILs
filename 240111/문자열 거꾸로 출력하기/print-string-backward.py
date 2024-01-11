s=[]

while True:
    x=input()
    if x=="END":
        for i in s:
            print(i)
        break
    x=x[::-1]
    s.append(x)
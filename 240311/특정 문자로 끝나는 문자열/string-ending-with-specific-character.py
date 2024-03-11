a=[]
for _ in range(10):
    x=input()
    a.append(x)
b=input()
s=[]
for i in a:
    if i[-1] == b:
        s.append(i)

if len(s)==0:
    print("None")
else:
    for i in s:
        print(i)
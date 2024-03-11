a=[]
for _ in range(10):
    x=input()
    a.append(x)
b=input()

for i in a:
    if i[-1] == b:
        print(i)
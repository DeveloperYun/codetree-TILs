n=int(input())
s=[]
a=0
b=0
for i in range(n):
    x=input()
    a+=len(x)
    if x[0]=='a':
        b+=1

print(a,b)
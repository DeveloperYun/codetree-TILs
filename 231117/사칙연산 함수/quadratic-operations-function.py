a,b,c=map(str,input().split())
a = int(a)
c = int(c)

if b=="+":
    print(a,"+",c,"=",a+c)
elif b=="-":
    print(a,"-",c,"=",a-c)
elif b=="/":
    print(a,"/",c,"=",a//c)
else:
    print(a,"*",c,"=",a*c)
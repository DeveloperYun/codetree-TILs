a,b=map(str,input().split())

a2=""
b2=""
for i in a:
    if '0'<=i<='9':
        a2+=i
    else:
        break

for i in b:
    if '0'<=i<='9':
        b2+=i
    else:
        break

a2=int(a2)
b2=int(b2)
print(a2+b2)
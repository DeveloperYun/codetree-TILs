a=list(map(str,input().split('.')))
b=''
for i in a:
    b += i
answer=''
for i in b:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        answer += i.upper()
print(answer)
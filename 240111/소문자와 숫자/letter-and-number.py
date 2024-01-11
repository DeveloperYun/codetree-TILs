a=input()
answer=''
for i in a:
    if i.isdigit():
        answer += i
    elif 'a'<=i<='z' or 'A'<=i<='Z':
        answer += i.lower()
print(answer)
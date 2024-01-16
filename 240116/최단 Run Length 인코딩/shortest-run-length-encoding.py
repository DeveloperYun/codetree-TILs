a=input()

answer=111

def encoding(st):
    complete=""
    curr = st[0]
    num_char = 1
    
    for i in st[1:]:
        if i == curr:
            num_char += 1
        else:
            complete += curr
            complete += str(num_char)

            curr = i
            num_char = 1
    complete += curr
    complete += str(num_char)

    return len(complete)

answer = encoding(a)

for i in range(len(a)):
    a=list(a)
    temp = a[-1]
    for j in range(len(a)-1,0,-1):
        a[j] = a[j-1]
    a[0] = temp
    a=''.join(a)
    answer = min(answer,encoding(a))
print(answer)
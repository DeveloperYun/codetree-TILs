lst = input()

def ch(a):
    b = a[0]
    for i in a:
        if i != b:
            return False
    return True

if ch(lst) == True:
    print('No')
else:
    print('Yes')
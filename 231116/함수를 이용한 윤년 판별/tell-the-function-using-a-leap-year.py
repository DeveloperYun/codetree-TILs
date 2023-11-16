def is_onjeonsu(n):
    if n % 4 == 0:
        return True
    if n % 4 == 0 and n%100 == 0:
        return False
    if n % 4 == 0 and n%100 == 0 and n%400 == 0:
        return True
    return False

n=int(input())
if is_onjeonsu(n)==True:
    print("true")
else:
    print("false")
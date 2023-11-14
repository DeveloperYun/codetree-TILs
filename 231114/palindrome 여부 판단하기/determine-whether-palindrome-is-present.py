a=input()

def answer(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            print("No")
            return
    else:
        print("Yes")
        return
answer(a)
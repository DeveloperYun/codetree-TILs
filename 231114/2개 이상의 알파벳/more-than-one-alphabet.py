s=input()

def answer(s):
    cnt=[0]*26

    for c in s:
        cnt[ord(c)-97] += 1
        if cnt[ord(c)-97] == 2:
            print("Yes")
            return
    
    print("No")
answer(s)
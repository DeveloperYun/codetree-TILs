a,b=map(int,input().split())

def answer(a,b):
    if a>b:
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25
    
    return [a,b]

ans=answer(a,b)
print(ans[0],ans[1])
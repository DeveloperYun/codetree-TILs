n=int(input())
s=list(map(int,input().split()))

def bubble():
    is_sortedd = False

    while not is_sortedd:
        is_sortedd=True
        for i in range(n-1):
            if s[i] > s[i+1]:
                s[i],s[i+1]=s[i+1],s[i]
                is_sortedd=False
    
bubble()
for i in s:
    print(i,end=" ")
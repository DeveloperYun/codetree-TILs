n=int(input())
s=list(map(int,input().split()))

def bubble():
    is_sortedd = False

    while not is_sortedd:
        for i in range(n-1):
            if s[i] > s[i+1]:
                s[i],s[i+1]=s[i+1],s[i]
                is_sortedd=True
    
bubble()
for i in s:
    print(i,end=" ")
from itertools import combinations

arr = list(map(int,input().split()))

arr.sort() 
# 3, 3, 4, 6, 7, 7, 7, 10, 10, 10, 11, 13, 14, 14, 17  

temp = list(combinations(arr,4))

def possible(x):
    a,b,c,d = x

    if (a+b in arr) and (b+c in arr) and (c+d in arr) and (d+a in arr) and (a+c in arr) and (b+d in arr) and (a+b+c in arr) and (a+b+d in arr) and (a+c+d in arr) and (b+c+d in arr) and  (a+b+c+d in arr):
        return True
    
    return False
for t in temp:
    # t = (3,3,4,6)
    if possible(t):
        for i in t:
            print(i,end=" ")
        break
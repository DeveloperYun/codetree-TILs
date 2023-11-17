from itertools import permutations

s=list(map(int,input().split()))
n=6

mindiff = 10000001

temp = list(permutations(s,6))

def answer(s1,s2,s3):
    global mindiff
    temp = []
    temp.append(s1)
    temp.append(s2)
    temp.append(s3)
    maxteam = max(temp)
    minteam = min(temp)

    if maxteam-minteam < mindiff:
        mindiff = maxteam-minteam
    
    return mindiff

for t in temp:
    s1 = t[0]+t[1]
    s2 = t[2]+t[3]
    s3 = t[4]+t[5]

    a=answer(s1,s2,s3)



print(a)
n=int(input())
data=[]
for _ in range(n):
    c,s=map(str,input().split())
    s=int(s)
    data.append((c,s))

answer=0
suma=0
sumb=0

state = []

for c, s in data:
    if c=="A":
        suma += s
    elif c=="B":
        sumb += s

    if sumb > suma:
        state.append('B')
    elif suma==sumb:
        state.append(['A','B'])
    else:
        state.append('A')

for i in range(1,len(state)):
    if state[i] != state[i-1]:
        answer += 1

if n==1:
    print(0)
else:
    print(answer+1)
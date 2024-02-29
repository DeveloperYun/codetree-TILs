n=int(input())
arr=[]
dic={}

for _ in range(n):
    x = input()
    x = ''.join(sorted(x))
    
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1

ans=0
for key, val in dic.items():
    ans = max(ans,val)
print(ans)
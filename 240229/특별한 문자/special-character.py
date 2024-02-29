x=input()

x = list(x)
dic={}

for i in x:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

ans=''
for key, val in dic.items():
    if val == 1:
        ans = key
        break
if ans=='':
    print("None")
else:
    print(ans)
import copy

n=int(input())
s=input() # 1000100100010

answer = 999999
for i in range(n):
    temp = copy.deepcopy(s)

    if temp[i] == 0:
        temp[i] = 1

        print(temp)
        
print(answer)
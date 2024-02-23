n,k=map(int,input().split())
coins=[]
for _ in range(n):
    x = int(input())
    coins.append(x)

#greedy 조건에 부합.
answer=0
while k!=0:
    if coins[-1] > k:
        coins.pop()
    
    answer += (k//coins[-1])
    k %= coins[-1]
    coins.pop()

print(answer)
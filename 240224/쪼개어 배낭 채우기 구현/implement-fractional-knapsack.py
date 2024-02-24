n,m=map(int,input().split())
jewelry=[]
for _ in range(n):
    w,v=map(int,input().split()) #무게, 가치
    std = round(v/w,3)
    jewelry.append((w,v,std))

jewelry.sort(lambda x:x[2], reverse=True)

answer=0
full_w=0
last_w=0
last_v=0
for jew in jewelry:
    weight, value, std = jew

    full_w += weight
    answer += value

    if full_w > m:
        last_w = weight
        last_v = value
        full_w -= weight
        answer -= value
        break

temp = m-full_w #8-4=4
x=temp/last_w
answer += (last_v*x)
answer = round(answer,3)
print(answer)
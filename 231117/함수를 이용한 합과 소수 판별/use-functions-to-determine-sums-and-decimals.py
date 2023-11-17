a,b=map(int,input().split())

def prime(x):
    
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
count=0
for i in range(a,b+1):
    #소수 판별
    if prime(i) == True:
        #자리수 합 구하기
        t1 = i//100
        t2 = i//10
        t3 = i%10

        if (t1+t2+t3)%2==0:
            count += 1

print(count)
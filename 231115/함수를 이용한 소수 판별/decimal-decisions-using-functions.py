# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
    if x==1:
        return False
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

s=0
def answer(a,b):
    global s
    for i in range(a,b+1):
        if is_prime_number(i):
            s+=i
a,b=map(int,input().split())
answer(a,b)
print(s)
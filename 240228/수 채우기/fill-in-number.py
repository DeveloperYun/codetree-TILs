import sys
n=int(input()) #만들고자하는 금액 
answer=0

if n<5 and n%2!=0:
    print(-1)
    sys.exit(0)
elif (n%5)%2==0:
    answer = (n//5) + (n%5)//2
else: #안 나누어 떨어지는거
    answer = ((n//5)-1) + ((n%5+5)//2)

print(answer)
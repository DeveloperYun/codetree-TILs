n=input()
n=list(n)
for i in range(len(n)):
    n[i] = int(n[i])

num=0
for i in range(len(n)):
    num = num*2+n[i]

num *= 17

digits=[]
while True:
    if num<2:
        digits.append(num)
        break
    
    digits.append(num%2)
    num//=2

for digit in digits[::-1]:
    print(digit,end="")
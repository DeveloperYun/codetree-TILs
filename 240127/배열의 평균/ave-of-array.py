a=list(map(int,input().split()))
b=list(map(int,input().split()))

print(f'{sum(a)/4:.1f}' , f'{sum(b)/4:.1f}')
print((a[0]+b[0])/2,(a[1]+b[1])/2,(a[2]+b[2])/2,(a[3]+b[3])/2)
print(f'{(sum(a)+sum(b))/8:.1f}')
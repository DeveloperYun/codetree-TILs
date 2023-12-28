x1,y1,x2,y2=map(int,input().split())
a1,b1,a2,b2=map(int,input().split())

max_r=2000
offset=1000

x1 += offset
x2 += offset
a1 += offset
a2 += offset
y1 += offset
y2 += offset
b1 += offset
b2 += offset

checked = [
    [0] *(max_r+1) for _ in range(max_r+1) 
]
answer = 0

if a1 <= x2 <= a2 and b1 <= y2 <= b2:
    answer = 0
elif a2 <=x1 and y2 >= b1:
    answer = abs(x1-x2)*abs(y2-y1)
elif b1 <= y2 <= b2 and a1 >= x2 >= a2:
    answer = abs(y2-y1)*abs(x1-x2)
elif b1 <= b2 <= b2 and x1 >= a2 >= x2:
    answer = abs(y2-y1)*abs(x1-a2)
elif a1 <= x1 <= a2 <= x2 and y1<=b1 <= y2 <= b2:
    answer = abs(x2-x1)*abs(y2-y1)
elif a2 <= x1 <= x2 and y1 <= b1 <= y2 <= b2:
    answer = abs(x2-x1)*abs(b1-y1)
elif a1 <= x1 <= a2 <= x2 and y1 <= b1 <= y2 <= b2:
    answer = abs(x2-x1)*abs(y2-y1)
elif a1 <= x1 <= a2 <= x2 and b1 <= y1 <= y2 <= b2:
    answer = abs(x2-a2) * abs(y2-y1)
elif a1 <= x1 <= x2 <= a2 and y1 <=b1<=y2<=b2:
    answer = abs(x2-x1)*abs(b1-y1)
else:
    answer = abs(x2-x1)*abs(y2-y1)

print(answer)
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

if a2 <= x2 <= x1 <= a1 and b1 <= y1 <= y2 <= b2:
    answer = 0
elif a2 <=x1 and y2 >= b1:
    answer = (x1-x2)*(y2-y1)
elif b1 <= y2 <= b2 and a1 >= x2 >= a2:
    answer = (y2-y1)*(x1-x2)
elif b1 <= b2 <= b2 and x1 >= a2 >= x2:
    answer = (y2-y1)*(x1-a2)
else:
    answer = (x2-x1)*(y2-y1)
print(answer)
m1,d1,m2,d2=map(int,input().split())
a=input()

def diff(m,d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0

    for i in range(1,m):
        total_days += days[i]

    total_days += d

    return total_days

gap = diff(m2,d2) - diff(m1,d1)

day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

if gap<7:
    idx=day_of_week.index(a)
    if idx < gap:
        print(idx)
else:
    print(gap//7+1)
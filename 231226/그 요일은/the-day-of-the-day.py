m1, d1, m2 ,d2 = tuple(map(int,input().split()))
day = input()

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']


def get_num(day):
    for i, elem in enumerate(days):
        if elem == day:
            return i

day_num = get_num(day)
d1 += day_num

elapsed_day = 0

def num_of_day(m, d):
    total_day = 0
    for i in range(1,m):
        total_day += month[i]
    total_day += d

    return total_day

elapsed_day = num_of_day(m2, d2) - num_of_day(m1,d1)

print(elapsed_day//7 +1)
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def get_season(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > 31:
        return -1
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap_year(year):
        days_in_month[2] = 29
    
    if day > days_in_month[month]:
        return -1

    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Fall"
    else:
        return "Winter"

# 입력 받기
year, month, day = map(int, input().split())

# 계절 출력 또는 -1 출력
result = get_season(year, month, day)
if result == -1:
    print(-1)
else:
    print(result)
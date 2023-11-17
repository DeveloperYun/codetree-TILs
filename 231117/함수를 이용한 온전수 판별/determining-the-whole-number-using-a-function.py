def cnt_onjeon_btwn(a, b) :
    cnt = 0
    for n in range(a, b+1) :
        if (n % 2 == 0) :
            continue
        elif (n % 10 == 5) :
            continue
        elif (n % 3 == 0) and (n % 9 != 0) :
            continue
        else :
            cnt += 1
    return print(cnt)

a, b = map(int, input().split())
cnt_onjeon_btwn(a, b)
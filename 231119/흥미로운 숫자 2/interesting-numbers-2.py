x, y = map(int, input().split())

cnt = 0
for i in range(x, y+1):

    n_arr = list(map(int, list(str(i))))
    n_dic = {}
    for n in n_arr:
        if n in n_dic:
            n_dic[n] += 1
        else:
            n_dic[n] = 1
    if len(n_dic) == 2 and 1 in n_dic.values():
        #print(i)
        cnt += 1
print(cnt)
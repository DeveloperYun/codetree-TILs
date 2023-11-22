from sys import stdin
base = [0 for _ in range(3)]
for i in range(3):
    base[i] = stdin.readline().strip()
# print(base)

cnt = set()
for i in range(3):
    check = set() #중복 제거
    for j in range(3):
        check.add(base[i][j])
    if len(check) == 2: #2가지로만 구성시 가능
        cnt.add(tuple(sorted(check)))

for j in range(3):
    check = set()
    for i in range(3):
        check.add(base[i][j])
    if len(check) == 2:
        cnt.add(tuple(sorted(check)))

check  = set()
for i in range(3):
    check.add(base[i][i])
if len(check) == 2:
        cnt.add(tuple(sorted(check)))

check  = set()
for i in range(3):
    check.add(base[i][3-1-i])
if len(check) == 2:
        cnt.add(tuple(sorted(check)))
print(len(cnt))
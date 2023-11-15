n, k = map(int, input().split())

setting = [0] * 101

for _ in range(n) :
    candy, index = map(int, input().split())
    setting[index] += candy

result = 0
# 처음부터 끝가지 완전탐색을 한다.
for i in range(101) :
    # cosider out of range
    max_value = 0
    for j in range(i - k, i + k + 1) :
        if j >= 0 and j < 101 :
            max_value += setting[j]
    result = max(result, max_value)    
print(result)
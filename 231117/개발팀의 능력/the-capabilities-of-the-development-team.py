arr = list(map(int, input().split()))

def find_minVal(i, j, k, s):
    sum1 = arr[i]+arr[j]
    sum2 = arr[k]+arr[s]
    sum3 = sum(arr) - (sum1+sum2)

    #능력이 가장 큰팀과 작은 팀의 차이
    min_val = float('inf')
    max_val = 0 

    min_val = min(sum1, sum2, sum3)
    max_val = max(sum1, sum2, sum3)

    calc = 0
    if(sum1 != sum2 and sum2!= sum3 and sum1 !=sum3):
        calc= max_val - min_val

    return calc
    

min_val = 10000001
#첫번째 매칭
for i in range(5):
    for j in range(i+1, 5):
        # 두 번째 매칭 
        for k in range(0, 5):
            for s in range(k+1, 5):
                if(i != k and j!= k and s!= i and s!= j):
                    cal = find_minVal(i,j,k,s)
                    if(cal != 0):
                        min_val = min(min_val,cal)

if min_val != 10000001:
    print(min_val)
else:
    print(-1)
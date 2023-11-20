n=int(input())
arr=list(map(int,input().split()))

min_diff=99999

for i in range(n):
    arr[i] *= 2 #2배

    for j in range(n):
        remaining_arr = []

        for k in range(n):
            if k != j:
                remaining_arr.append(arr[k])

        
        sum_diff = 0

        for k in range(n-2):
            sum_diff += abs(remaining_arr[k+1] - remaining_arr[k])
        
        min_diff= min(min_diff,sum_diff)
    
    arr[i] //= 2

print(min_diff)
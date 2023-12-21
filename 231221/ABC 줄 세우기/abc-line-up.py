import copy
import sys
n=int(input())
arr=list(map(str,input().split()))

for i in range(n):
    arr[i] = ord(arr[i])

#case1) 처음부터 모두 정렬된 상태
temp = copy.deepcopy(arr)
if arr == temp:
    print("0")
    sys.exit(0)
#arr : 65 68 66 67

sorted_arr = sorted(temp)

answer = 0

while True:
    if sorted_arr == arr:
        print(answer)
        break
    
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            answer += 1
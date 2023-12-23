n=int(input())
arr=list(map(int,input().split()))

answer=0

def count_positive_numbers(num1, num2, num3):
    # 각 수가 양수인지 확인하고 양수의 개수를 센다
    positive_count = 0
    if num1 > 0:
        positive_count += 1
    if num2 > 0:
        positive_count += 1
    if num3 > 0:
        positive_count += 1

    # 양수의 개수가 2개인지 아닌지를 판단한다
    if positive_count == 2:
        return True
    else:
        return False

def classify_numbers(num1, num2, num3):
    # 각 수가 양수인지 음수인지 확인
    positive_count = 0
    negative_count = 0

    if num1 > 0:
        positive_count += 1
    elif num1 < 0:
        negative_count += 1

    if num2 > 0:
        positive_count += 1
    elif num2 < 0:
        negative_count += 1

    if num3 > 0:
        positive_count += 1
    elif num3 < 0:
        negative_count += 1

    # 양수가 하나이고 음수가 둘이면 True를 반환
    if positive_count == 1 and negative_count == 2:
        return True
    else:
        return False

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            #case1 : 셋다 양수
            if arr[i] > 0 and arr[j] > 0 and arr[k] > 0:
                answer = max(answer,arr[i]*arr[j]*arr[k])
            #case2 : 셋 중 둘이 양수
            elif count_positive_numbers(arr[i],arr[j],arr[k]):
                answer = max(answer,arr[i]*arr[j]*arr[k])
            #case3 : 셋 중 하나가 양수, 둘이 음수
            elif classify_numbers(arr[i],arr[j],arr[k]):
                answer = max(answer,arr[i]*arr[j]*arr[k])

print(answer)
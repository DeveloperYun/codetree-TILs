import sys
n,s=map(int,input().split())
arr=list(map(int,input().split()))

#정수 s = 20
#정수 6개 - 6개의 수들 중 정확히 2개를 제외하여 남은
#           4개의 숫자들의 합이 20이랑 최대한 가까워지도록

answer=sys.maxsize

for i in range(n):
    for j in range(i+1,n):
        #숫자 arr[i], arr[j]를 제외
        temp_sum = sum(arr) - arr[i] - arr[j]

        temp = abs(s-temp_sum)
        if temp < answer:
            answer = temp

print(answer)
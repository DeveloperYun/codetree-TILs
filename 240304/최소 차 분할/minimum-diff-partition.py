n=int(input())
arr=list(map(int,input().split()))

#두 그룹의 합의 차가 최소가 되려면 ?
'''
dp[i] = i번째 숫자를 그룹에 포함했을 때. 
'''
arr.sort() # 4,5,7,8,9
answer=99999999

for i in range(n-1):
    temp1 = sum(arr[:i+1])
    temp2 = sum(arr[i+1:])

    answer = min(answer, abs(temp1-temp2))

print(answer)
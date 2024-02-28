n=int(input())
arr=list(map(int,input().split()))


answer=[]
while len(arr) > 1:
    # 단순하게 그냥 arr을 정렬해뒀으니까
    # 가장 앞에 위치한 2개가 가장 작은 숫자, 즉 더해야하는 숫자다.
    arr.sort() #가장 작은 2개를 고르기 위해서 정렬한다.

    a,b=arr[0],arr[1]
    temp = a+b
    answer.append(temp)
    arr.pop(0)
    arr.pop(0)
    arr.insert(0,temp)

print(sum(answer))
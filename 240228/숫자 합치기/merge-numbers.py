import heapq

n=int(input())
arr=list(map(int,input().split()))
heap=[]

for i in arr:
    heapq.heappush(heap,i)

answer=[]
while len(heap) > 1:
    # 단순하게 그냥 arr을 정렬해뒀으니까
    # 가장 앞에 위치한 2개가 가장 작은 숫자, 즉 더해야하는 숫자다.
    
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    temp = a+b
    answer.append(temp)
    
    heapq.heappush(heap,temp)

print(sum(answer))
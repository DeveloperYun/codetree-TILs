n=int(input())
arr=list(map(int,input().split()))

def heapify(arr,n,i):
    largest = i
    left = i*2
    right = i*2+1

    if left <= n and arr[left] > arr[largest]:
        largest = left

    if right <= n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(largest)

def heapsort(arr,n):
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)
    
    for i in range(n,1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i-1,1)
arr,sort()
for i in arr:
    print(i,end=" ")
n=int(input())
arr=list(map(int,input().split()))

def insertion():
    for i in range(1,n):
        j = i-1
        key = arr[i]

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
arr.sort()
for i in arr:
    print(i,end=" ")
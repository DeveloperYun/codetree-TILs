def selection(arr):
    sizes = len(arr)

    for i in range(sizes-1):
        mini = i

        for j in range(i+1,sizes):
            if arr[j] < arr[mini]:
                mini = j
            
            temp = arr[i]
            arr[i] = arr[mini]
            arr[mini] = temp
    
    return arr

n=int(input())
w=list(map(int,input().split()))

a=sorted(w)
for i in a:
    print(i,end=" ")
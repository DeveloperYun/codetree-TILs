arr=[
    [1]*5 for _ in range(5)
]

for i in range(1,5):
    for j in range(1,5):
        arr[i][j] = arr[i][j-1]+arr[i-1][j]

for i in range(5):
    for j in range(5):
        print(arr[i][j],end=' ')
    print()
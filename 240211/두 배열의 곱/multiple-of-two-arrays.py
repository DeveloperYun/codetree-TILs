arr1 = []
for i in range(3):
    temp = list(map(int,input().split()))
    arr1.append(temp)
a=input()
arr2 = []
for i in range(3):
    temp = list(map(int,input().split()))
    arr2.append(temp)
    
for i in range(3):
    for j in range(3):
        print(arr1[i][j]*arr2[i][j],end=" ")
    print()
from collections import Counter

n,k=map(int,input().split())
arr=[
    int(input()) for _ in range(n)
]

def cnt(temp):
    #temp = [7,2,4,2]
    counts = Counter(temp)
    most_common = counts.most_common(1) #(2,2)(2,3)(4,2)
    
    return most_common
        

answer=[]
for i in range(n-k):
    temp = []
    for j in range(i,i+k+1):
        temp.append(arr[j])    
    s = cnt(temp)
    answer.append(s)

unwrapped_list = [item[0] for item in answer]
unwrapped_list.sort(key=lambda x:x[1], reverse=True)
print(unwrapped_list[0][0])
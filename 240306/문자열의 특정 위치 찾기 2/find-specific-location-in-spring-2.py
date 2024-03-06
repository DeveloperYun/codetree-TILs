s=["apple", "banana", "grape", "blueberry", "orange"]
a=input()
x=0
for i in s:
    if i[2]==a or i[3]==a:
        print(i)
        x+=1
print(x)
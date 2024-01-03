n, k = map(int, input().split())
answer = []

def Print() :
    for e in answer :
        print(e, end = ' ')
    print() 

def check(num) :
    if num == k + 1 :
        Print()
        return

    for i in range(1, n + 1) :
        answer.append(i)
        check(num + 1)
        answer.pop()
    return 

check(1)
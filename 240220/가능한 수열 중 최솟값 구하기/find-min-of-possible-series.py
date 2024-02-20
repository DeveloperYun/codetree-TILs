n=int(input())

answer=[]
seq = [] #가능한 모든 조합이 담긴다.

def check(sequence):
    
    for i in range(len(sequence)-1):
        if sequence[i] == sequence[i+1]:
            return False

    return True


def find_min(idx):
    global answer

    if len(seq)==n:
        if check(seq):
            temp = seq[:]
            answer.append(temp)
        return

    for i in range(4,6+1):
        seq.append(i)
        find_min(idx+1)
        seq.pop()

find_min(0)
answer.sort()
a=answer[0]
for i in a:
    print(i,end='')
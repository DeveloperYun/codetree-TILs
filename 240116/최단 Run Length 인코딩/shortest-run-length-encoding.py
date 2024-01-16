input = input()
input = list(input)
n = len(input)

def RL_encoding():
    res = ""
    cnt = 1
    if n == 1:
        return 2
    
    for i in range(n-1):
        if input[i] == input[i+1]:
            cnt += 1
            if i == n-2:
                res += input[i]
                res += str(cnt)
                break
        else: 
            res += input[i]
            res += str(cnt)
            cnt = 1
            if i == n-2:
                res += input[i+1]
                res += str(cnt)
                break   
            
    return len(res)


def push():
    tmp = input[n-1]
    for i in range(n-1, 0, -1):
        input[i] = input[i-1]
    input[0] = tmp

min_len = 11111
for _ in range(n):
    min_len = min(min_len, RL_encoding())
    push()

print(min_len)
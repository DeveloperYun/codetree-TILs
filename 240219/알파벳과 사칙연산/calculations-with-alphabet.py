formula = input()
answer=-999999999999
n = 6
num = [0 for _ in range(n)] #a~f와 매핑되는 수를 의미 

#formula = 'a+a-a+a*a-a'
#ord = 문자에 해당하는 유니코드 정수 
def conv(idx): #num의 idx 항을 숫자로 반환 0, 2, 4, 6, ...
    index = ord(formula[idx]) - ord('a')
    return num[index]

def calculate():
    length = len(formula)
    result = conv(0) 

    for i in range(2, length, 2):
        if formula[i-1] == '+':
            result += conv(i)
        elif formula[i-1] == '-':
            result -= conv(i)
        else:
            result *= conv(i)
    
    return result
    
def backtracking(curr_idx):
    global answer

    if curr_idx == n: 
        #alphabet과 operand로 새로운 식을 만든다.
        answer = max(answer,calculate())
        return
    

    for i in range(1,5): #1~4
        num[curr_idx] = i
        backtracking(curr_idx+1)

backtracking(0)
print(answer)
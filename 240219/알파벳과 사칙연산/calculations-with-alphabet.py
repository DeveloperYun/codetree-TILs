formula = input()
answer=-999999999999
n = len(formula)
alphabet_n = n - (n//2) #알파벳의 개수 

def calculate(exps):
    # 3-1*b
    result = 0
    numbers=[]
    ops=[]
    for i in exps:
        if '1'<=i<='4':
            numbers.append(int(i))
        else:
            ops.append(i)
    
    for op in ops:
        a1 = numbers.pop(0)
        a2 = numbers.pop(0)
        temp = 0
        if op=='+':
            temp = a1+a2
        elif op == '-':
            temp = a1-a2
        elif op == '*':
            temp = a1*a2
        
        numbers.insert(0,temp)
    
    result = numbers[0]
    return result
    
alphabet=[]
operand=[]
for i in formula:
    if i<'a' or i>'f':
        operand.append(i)

def check(alpha):
    formula2 = []
    for i in formula:
        if 'a' <= i <= 'f':
            formula2.append(i)
    
    alpha2 = []
    for i in alpha:
        if '1'<=i<='4':
            alpha2.append(i)

    dic = {}
    for idx,val in enumerate(formula2):
        if val not in dic:
            dic[val] = alpha2[idx]
        elif dic[val] != alpha2[idx]:
            return False
    
    return True


    
def backtracking(curr_idx):
    global answer

    if curr_idx == alphabet_n: 
        #alphabet과 operand로 새로운 식을 만든다.
        expression = ''
        for k in range(len(operand)):
            expression+=alphabet[k]
            expression+=operand[k]
        expression+=alphabet[-1]
        if check(expression):
            answer = max(answer,calculate(expression))
        return
    

    for i in range(1,5): #1~4
        alphabet.append(str(i))
        backtracking(curr_idx+1)
        alphabet.pop()

backtracking(0)
print(answer)
n=int(input())
st = input()

answer_cnt = 0

# i x m v d k i x m v
# i   j
x=0
for i in range(n-1):
    for j in range(i+1, n):
        temp = []
        for k in range(i,j+1):
            temp.append(st[k])
        test = ''.join(temp)
        cnt = st.count(test)
        
        if cnt >= answer_cnt:
            answer_cnt = cnt
            t=len(test)
            x=max(x,t)
            
        
print(x+1)
n=int(input())
st = input()

answer_cnt = 0

# i x m v d k i x m v
# i   j
x=0
member = []
for i in range(n-1):
    for j in range(i+1, n):
        temp = []
        for k in range(i,j+1):
            temp.append(st[k])
        test = ''.join(temp)
        cnt = st.count(test) #test가 문자열에 몇 개 있는지 확인 
        
        if cnt >= answer_cnt:
            answer_cnt = cnt
            t=len(test)
            member.append((len(test),answer_cnt))

member.sort(key = lambda x:x[1], reverse=True)
k = member[0][1] #2
answer=0
for i in member:
    #i = (2,2)
    if i[1] == k:
        answer = max(answer,i[0])
print(answer+1)
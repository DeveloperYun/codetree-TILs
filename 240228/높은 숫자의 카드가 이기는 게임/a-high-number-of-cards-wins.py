n=int(input())
card_b = []
for _ in range(n):
    x=int(input())
    card_b.append(x)

card = [x for x in range(1,2*n+1)]
card_a = []
for i in card:
    if i not in card_b:
        card_a.append(i)

answer=0 #A가 이기는 횟수 

#B를 순회하면서
#B[i]보다 큰 값들을 후보로 넣고
#후보 중에서 차이가 가장 작은 값을 pick 한뒤에 pop시키고 동시에 answer + 1 한다.

for i in card_b:
    temp = [k for k in card_a if k > i]
    if temp:
        min_diff_value = min(temp, key=lambda x: x - i)
        card_a.remove(min_diff_value)
        answer += 1

print(answer)
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

card_a.sort()
card_b.sort()

for i in range(n):
    if card_b[i] > card_a[i]:
        answer += 1
print(answer)
a, b = tuple(map(int, input().split()))   # A 구역 입력 
c, d = tuple(map(int, input().split()))   # B 구역 입력 

area = [0] * 101   # 청소 구역 모두 0으로 초기화 한 리스트 만들기 

for i in range(a, b):   # A 구역 1로 채워놓기 
    area[i] = 1

for j in range(c, d):   # B 구역 1로 채워놓가 (A와 중복된 경우 1 그대로 유지되므로 상관 X)
    area[j] = 1

print(area.count(1))   # 청소 구역 중 1의 개수 = 청소된 구역 개수
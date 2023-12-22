n = int(input())
numbers = list(map(int, input().split()))

# 중복을 제거한 숫자들을 저장한 리스트를 만듭니다.
unique_numbers = list(set(numbers))

# 만약 숫자의 개수가 1 이하이면 두 번째로 작은 숫자가 없으므로 -1을 출력합니다.
if len(unique_numbers) <= 1:
    print(-1)
else:
    # 중복을 제거한 숫자들을 정렬합니다.
    unique_numbers.sort()

    # 두 번째로 작은 숫자를 찾습니다.
    second_smallest = unique_numbers[1]

    # 두 번째로 작은 숫자가 여러 개인 경우 -1을 출력합니다.
    if numbers.count(second_smallest) > 1:
        print(-1)
    else:
        # 두 번째로 작은 숫자의 위치를 찾아 출력합니다.
        position = numbers.index(second_smallest) + 1
        print(position)
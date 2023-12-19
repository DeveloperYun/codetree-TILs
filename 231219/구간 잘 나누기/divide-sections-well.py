def min_max_sum(nums, m, mid):
    cnt = 1
    cur_sum = 0

    for num in nums:
        cur_sum += num
        if cur_sum > mid:
            cnt += 1
            cur_sum = num

    return cnt <= m


def find_min_max_sum(nums, m):
    start, end = max(nums), sum(nums)
    result = 0

    while start <= end:
        mid = (start + end) // 2

        if min_max_sum(nums, m, mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result

n, m = map(int, input().split())
nums = list(map(int, input().split()))

answer = find_min_max_sum(nums, m)
print(answer)
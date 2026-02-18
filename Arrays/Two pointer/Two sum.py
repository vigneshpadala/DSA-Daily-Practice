def two_sum(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        sum1 = arr[l] + arr[r]

        if sum1 == target:
            return [l,r]
        elif sum1 > target:
            r -= 1
        else:
            l += 1

    return -1  # if not found


arr = [1, 2, 5, 9, 10]
target = 7

print(two_sum(arr, target))

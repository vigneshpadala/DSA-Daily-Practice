# ️Maximum Window Sum

# Given an integer array arr and an integer k,
# find the maximum sum of any contiguous subarray of size k.

def max_sum(arr, k):
    n = len(arr) - 1

    if (n <= k):
        print("invalid")
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[k + 1]
        max_sum = max(window_sum, max_sum)
    return max_sum


arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 4
print(max_sum(arr, k))

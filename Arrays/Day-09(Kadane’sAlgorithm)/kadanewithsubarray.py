#Using Kadane’s Algorithm with indices

def kadane_with_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    start = end = temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, arr[start:end+1]


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum_, subarray = kadane_with_subarray(arr)

print("Sum =", sum_)
print("Subarray =", subarray)

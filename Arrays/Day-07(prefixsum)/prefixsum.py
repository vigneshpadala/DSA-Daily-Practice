# Prefix Sum:
# Prefix Sum means:
# Precompute cumulative sums so that range-sum queries become fast.
# Instead of calculating sum again and again ❌
# We calculate it once and reuse it ✅

# problem:
arr = [2, 1, 4, 6, 3]
prefix_sum = []
prefix_sum.append(arr[0])
for i in range(1, len(arr)):
    prefix_sum.append(prefix_sum[i-1] + arr[i])
print(prefix_sum)

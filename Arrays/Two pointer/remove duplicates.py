def remove_duplicates(arr):
    if not arr:
        return arr

    l = 0

    for r in range(1, len(arr)):
        if arr[l] != arr[r]:
            l += 1
            arr[l] = arr[r]

    return arr[:l+1]


arr = [1, 1, 2, 2, 5, 9, 9, 10]
print(remove_duplicates(arr))
